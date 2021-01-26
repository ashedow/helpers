# Consul
> By HashiCorp

Consul is a tool for discovering and configuring services in your infrastructure. Consul's key features include service discovery, health checking, a KV store, and robust support for multi-datacenter deployments. 

## Terminology

* Nomad Server: Nomad servers are the brains of the cluster; they receive and allocate jobs to Nomad clients. In CircleCI, a Nomad server runs on your Services machine as a Docker Container.

* Nomad Client: Nomad clients execute the jobs they are allocated by Nomad servers. Usually a Nomad client runs on a dedicated machine (often a VM) in order to fully take the advantage of machine power. You can have multiple Nomad clients to form a cluster and the Nomad server allocates jobs to the cluster with its scheduling algorithm.

* Nomad Jobs: A Nomad job is a specification, provided by a user, that declares a workload for Nomad. In CircleCI 2.0, a Nomad job corresponds to an execution of a CircleCI job. If the job uses parallelism, say 10 parallelism, then Nomad will run 10 jobs.

* Build Agent: Build Agent is a Go program written by CircleCI that executes steps in a job and reports the results. Build Agent is executed as the main process inside a Nomad Job.

## Usefull commands

Checking the Jobs Status
```
nomad status
```

Checking the Cluster Status
```
nomad node-status
```

Checking Logs
```
nomad logs -job -stderr <nomad-job-id>
```

To get more information about a specific client, run the following from that client with key `-self`

## Links
https://www.consul.io/