# Custom Dockerfile
FROM apache/airflow:2.0.1

# Install dependencies
# It's more efficient to do pip install here than adding a requirements.txt
USER root
# RUN apt-get update -yqq \
#     && apt-get install -y gcc freetds-dev \
#     && apt-get install -y git procps \ 
#     && pip install apache-airflow

# This fixes permission issues on linux. 
# The airflow user should have the same UID as the user running docker on the host system.
ARG DOCKER_UID
RUN \
    : "${DOCKER_UID:?Build argument DOCKER_UID needs to be set and non-empty. Use 'make build' to set it automatically.}" \
    && usermod -u ${DOCKER_UID} airflow \
    && echo "Set airflow's uid to ${DOCKER_UID}"

USER airflow

# docker build --build-arg DOCKER_UID=`id -u` --rm -t custom-airflow .
