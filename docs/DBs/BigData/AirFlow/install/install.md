# Install AirFlow in Docker

## Before you begin

Follow these steps to install the necessary tools.
* Install Docker Community Edition (CE) on your workstation.
* Install Docker Compose v1.27.0 and newer on your workstation.
Older versions of docker-compose do not support all features required by docker-compose.yaml file, so double check that it meets the minimum version requirements.

Fetch or get docker-compose.yaml
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml'
```

This file contains several service definitions:

* `airflow-scheduler` - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.
* `airflow-webserver` - The webserver available at http://localhost:8080.
* `airflow-worker` - The worker that executes the tasks given by the scheduler.
* `airflow-init` - The initialization service.
* `flower` - The flower app for monitoring the environment. It is available at http://localhost:8080.
* `postgres` - The database.
* `redis` - The redis - broker that forwards messages from scheduler to worker.

All these services allow you to run Airflow with [CeleryExecutor](https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html). For more information, see [Basic Airflow architecture](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#architecture).

Some directories in the container are mounted, which means that their contents are synchronized between your computer and the container.

* `./dags` - you can put your DAG files here.
* `./logs` - contains logs from task execution and scheduler.
* `./plugins` - you can put your [custom plugins](https://airflow.apache.org/docs/apache-airflow/stable/plugins.html) here.

## Initializing Environment

Prepare your environment, i.e. create the necessary files, directories and initialize the database.

On **Linux**, the mounted volumes in container use the native Linux filesystem `user/group` permissions, so you have to make sure the container and host computer have matching file permissions.
```bash
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

On all operating system, you need to run database migrations and create the first user account. To do it, run.
```bash
docker-compose up airflow-init
```

After initialization is complete, you should see a message like below.
```sh
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.0.1
start_airflow-init_1 exited with code 0
```
The account created has the login `airflow` and the password `airflow`.

Running Airflow
Now you can start all services:
```bash
docker-compose up --detach
```
In the second terminal you can check the condition of the containers and make sure that no containers are in unhealthy condition:
```bash
$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                              NAMES
247ebe6cf87a   apache/airflow:2.0.1   "/usr/bin/dumb-init …"   3 minutes ago    Up 3 minutes              8080/tcp                           compose_airflow-worker_1
ed9b09fc84b1   apache/airflow:2.0.1   "/usr/bin/dumb-init …"   3 minutes ago    Up 3 minutes              8080/tcp                           compose_airflow-scheduler_1
65ac1da2c219   apache/airflow:2.0.1   "/usr/bin/dumb-init …"   3 minutes ago    Up 3 minutes (healthy)    0.0.0.0:5555->5555/tcp, 8080/tcp   compose_flower_1
7cb1fb603a98   apache/airflow:2.0.1   "/usr/bin/dumb-init …"   3 minutes ago    Up 3 minutes (healthy)    0.0.0.0:8080->8080/tcp             compose_airflow-webserver_1
74f3bbe506eb   postgres:13            "docker-entrypoint.s…"   18 minutes ago   Up 17 minutes (healthy)   5432/tcp                           compose_postgres_1
0bd6576d23cb   redis:latest           "docker-entrypoint.s…"   10 hours ago     Up 17 minutes (healthy)   0.0.0.0:6379->6379/tcp             compose_redis_1
```

## Accessing the environment

After starting Airflow, you can interact with it in 3 ways;
* by running [CLI commands](https://airflow.apache.org/docs/apache-airflow/stable/usage-cli.html).
* via a browser using [the web interface](https://airflow.apache.org/docs/apache-airflow/stable/ui.html).
* using the [REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html).

### Running the CLI commands
You can also run CLI commands, but you have to do it in one of the defined `airflow-*` services. For example, to run airflow info, run the following command:
```bash
docker-compose run airflow-worker airflow info
```
If you have Linux or Mac OS, you can make your work easier and download a optional wrapper scripts that will allow you to run commands with a simpler command.
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/airflow.sh'
chmod +x airflow.sh
```
Now you can run commands easier.
```bash
./airflow.sh info
```
You can also use `bash` as parameter to enter interactive bash shell in the container or python to enter python container.
```bash
./airflow.sh bash
```
```bash
./airflow.sh python
```

### Accessing the web interface
Once the cluster has started up, you can log in to the web interface and try to run some tasks.

The webserver available at: `http://localhost:8080`. The default account has the login `airflow` and the password `airflow`.

### Sending requests to the REST API

Basic username password authentication is currently supported for the REST API, which means you can use common tools to send requests to the API.

The webserver available at: `http://localhost:8080`. The default account has the login `airflow` and the password `airflow`.

Here is a sample `curl` command, which sends a request to retrieve a pool list:
```bash
ENDPOINT_URL="http://localhost:8080/"
curl -X GET  \
    --user "airflow:airflow" \
    "${ENDPOINT_URL}/api/v1/pools"
```

## Cleaning up

To stop and delete containers, delete volumes with database data and download images, run:
```bash
docker-compose down --volumes --rmi all
```

## Notes
By default, the Docker Compose file uses the latest Airflow image (apache/airflow). If you need, you can [customize and extend it](https://airflow.apache.org/docs/apache-airflow/stable/production-deployment.html#docker-image).

# Run Airflow in Docker-Compose. Airflow.cfg, Metadata DB

In `AIRFLOW_HOME` directory you can find `airflow.cfg` config that contains all settings for web-server, workers, scheduler and other Airflow services. Executor type and parameters, metadata DB connection details and many other options are also there. Official documentation will give a basic idea of airflow.cfg structure.
> https://airflow.apache.org/howto/set-config.html 
> https://github.com/apache/airflow/blob/master/airflow/config_templates/default_airflow.cfg#L32

Previously we worked using default settings with SequentialExecutor and SQLite DB.

Now, we will create Apache Airflow infrastructure that will be closer to production setup.

For that, we will use Docker and Docker-compose. If you prefer to stay on without Docker you can reproduce the same infrastructure in the local environment.

List of goals we’re going to achieve:
- Switch to CeleryExecutor and start several airflow workers.
- Run airflow scheduler in a dedicated container.
- Run airflow webserver in a dedicated container.
- Use PostgreSQL as Airflow metadata DB.
- Use Redis as a broker between scheduler and workers.

If you have never heard about Celery, you can read the official documentation - https://docs.celeryproject.org/en/latest/. 
Tl;Dr: Celery is a Python task queue with focus on real-time processing, it means that Celery distributes tasks over several workers, that execute them in parallel and return results of the tasks. Celery is also used as Scheduler in many Python projects, But in Apache Airflow it is used only as executor with workers.

> Notice that the entire `$AIRFLOW_HOME` directory (which is `/usr/local/airflow` in the image used) is mounted from the host file system. Entrypoint has also been set explicitly to avoid configuration modification by image’s built-in startup script.

> https://github.com/apache/airflow/blob/master/IMAGES.rst#airflow-docker-images

# Pip install 

You can install airflow with **additional dependencies**, for which you need to use something like `pip install apache-airflow[postgres,s3]`.

In order to learn more about extras with installation look at: https://airflow.apache.org/installation.html 


When you first time go to Airflow UI, it will require a username and password. For this, you have to create user using the following command: `airflow users create --username username --firstname firstname --lastname lastname --role Admin --email email --password password`

## Possible errors and solutions during run and installation:

1. RuntimeError in process of use command: `pip install apache-airflow`
Error:
RuntimeError: By default one of Airflow’s dependencies installs a GPL dependency (unidecode). To avoid this dependency set SLUGIFY_USES_TEXT_UNIDECODE=yes in your environment when you install or upgrade Airflow. To force installing the GPL version set AIRFLOW_GPL_UNIDECODE

Solution:
```bash
export SLUGIFY_USES_TEXT_UNIDECODE=yes
```
and re-run pip install with `pip install apache-airflow`


2. Command:
```
airflow scheduler
```
Error:
```
return __import__('MySQLdb')
ImportError: No module named MySQLdb
```
Solution:
```
pip install mysqlclient
```

## Link 
https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

