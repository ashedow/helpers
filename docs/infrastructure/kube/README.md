# Kubernetes
Just read [documentation](https://kubernetes.io/docs/home/)

etcd
API server
Controller-manager
Scheduler
kubelet

## Namespaces
Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called namespaces.

Namespaces provide a scope for names. Names of resources need to be unique within a namespace, but not across namespaces. Namespaces cannot be nested inside one another and each Kubernetes resource can only be in one namespace.

list the current namespaces in a cluster using:
```bash
kubectl get namespace
```

Kubernetes starts with four initial namespaces:

* `default` The default namespace for objects with no other namespace
* `kube-system` The namespace for objects created by the Kubernetes system
* `kube-public` This namespace is created automatically and is readable by all users (including those not authenticated). This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a requirement.
* `kube-node-lease` This namespace for the lease objects associated with each node which improves the performance of the node heartbeats as the cluster scales.

Create a new YAML file called my-namespace.yaml with the contents:
> Note: Avoid creating namespace with prefix kube-, since it is reserved for Kubernetes system namespaces.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: <insert-namespace-name-here>
```
Then run:
```bash
kubectl create -f ./my-namespace.yaml
```
Alternatively, you can create namespace using below command:
```bash
kubectl create namespace <insert-namespace-name-here>
```


## Use or not to use?

Criterias:
* Time to release
* Automated builds, deploy, tests
* CI/CD
* Amounts of efforts

Value for release eng:
* Immutable infrastructure + Infrastructure as code
* Idempotency
* One-button-release
* Time to rollback
* Introspection/issue investigation
* CD

Misconceptions:
* Container is a lightweight VM
* Kubernetes makes your app more secure
* Kubernetes makes your app scalable out of the box
* Kubernetes works out of the box on every OS without any problem

Experience: Observation
- Needs a lot of effort and additional applications for production
- Large stack to study
- We must care about several new ‘very important’ components
+ We should do it once (for all future projects)

Helm:
* Kubernetes package manager
* Client (helm) + Server (Tiller: etcd)
* Chart (helm package): Chart.yaml, templates, values
* Install + Rollback + Download from Repo + Plugins
* We run one tiller per namespace to reduce influence
* Tiller uses additional etcd, doesn’t rely on k8s concepts we run one tiller per namespace

Examples of configs:
* puppet/chef/ansible -> BOOMer
* compare boomer configs vs k8s yaml vs helm yaml

> Кубер all in one but need more for helm and kube

Clusters: Use next several clusters
* e2e - for internal testing
* prod, stage (should mimic prod) - as usual
* admin:
    * CI (the largest usage currently),
    * consolidated VPN (soon),
    * interVPC configuration (soon)
    * ...

Experience: CoreOS evaluation
* CloudFormation or TF
* No introspection to the state
* Problems: to update cluster, order of actions
* -> Stability risks

Experience: Internal Image Registry
* Private image registry (Docker Distribution) [3]
* High maintenance costs:
    * Need resilience (ssd fail, network fail, host fail)
    * GC (a lot of obsolete and very large images/layers)
    * High throughput (32 k8s workers need to download 2GB image)
* Quay as an external repo [4]
* Mostly private images: Secrets -> imagePullSecrets

Experience: kops
* Early adopters
* Doesn’t fully support CoreOS, fine with Debian8 (default)
* HA masters, idempotency (state-sync model), support addons, ...
* 0-downtime while doing rolling upgrade (multimaster)
* Multi-cloud / multi-region cluster

Experience: Networking
* Plenty of options [23]
* kops supports some of them (Calico, Weave, Flannel, ...)
* Possible to use other CNI provider
* Better use popular: better testing

Experience: Calico
* Works well with minimal issues
* Uses BGP, faster then any provider with encapsulation
* IP-in-IP encapsulation for multi-AZ or multi-cloud deployments [12]
* IP-in-IP: off, always, cross-subnet
* Calico also supports the NetworkPolicy integration (isolate traffic by labels)

Experience: HA
* 3 Masters, sync by etcd (for control-plane). May be 5/7/9 masters
* Bug in the upgrade process, we use etcd.v2 (will update to etcd.v3 shortly)

Experience: Disaster recovery
* We have a special cluster for all experiments and testing update procedure
* We take snapshots of volumes during risky updates


Experience: Access to k8s
* RBAC (Role-Based Access Control) is much nicer than ABAC
* Dex is an OpenID provider to integrate with your source of truth [6]
* Login script from console
* Alternative: go to Dex UI, login, copy-paste into ~/.kube/config

Experience: User Management
* Active Directory as source of truth (historic reasons)
* LDAP support for OpenVPN, Dex and Grafana to authenticate users
* Group information -> Roles in k8s

Experience: Access to AWS
* Only for Infra team (others - only if VERY needed)
* No long-term admin access keys, use temporary credentials instead
* Keys rotation
* Awsudo [7]

Experience: Quota Enforcement
* RBAC, access restrictions are on namespace per team
* Minimal set of quotas per team namespace
* for now - only object count
* later: CPU and Memory

Experience: Autoscaling
* AWS Cluster Autoscaler (vertical + horizontal) [8]
* Spot pricing to be added
* (It’s not Horizontal Pod Autoscaling)


Experience: Telemetry

Experience: Telemetry Framework
* Sensu is a poor fit, we want more metrics-focused approach [13]
* Prometheus has good query language and alerts, good balance [16]
* InfluxDB + rest of TICK stack (Deis). UI is nice, SQL-like query language is ok, but lack of features we need [14]

Experience: Cernan [15]
* Multiple interfaces for ingestion (sources)
* Emit to multiple aggregation sources (sinks)
* In-flight data manipulation (log lines to telemetry or vice versa) (filters)
* Written in Rust

Experience: Metrics
* Need to smoothly move from current infra (Statsd/Cernan)
* Prometheus would scrape data from Cernan
* Later: endpoints in all services to scrape data
* Current: DaemonSet / Sidecar containers
* Currently: WaveFront + instance of wavefront proxy in every cluster

Experience: Logging
* Requirement: no additional actions from user. Just print to stdout/stderr
* Cernan -> ElasticSearch
* k8s events -> ElasticSearch via Heapster [17]
* Kibana
* View logs with Stern (nice log tailor for k8s) [18]

Experience: Security and Secrets
* Legacy secrets management system (S3 buckets with KMS encrypted files)
* Kubernetes Secrets have alpha support for encryption as of 1.7
* Vault?


Experience: Development in k8s

Experience: Developer’s hell
* Docker way
* Tradeoff-s:
    * Create Image in CI Pipeline <-> Update Image FS on the fly
    * Run tests locally <-> Commit for CI to test
    * Run dependencies <-> Mock dependencies

Experience: Developer Tools
* Deis Workflow: very simple to use (Heroku-style), can’t support all our use cases
* Helm Charts: nice, simple. Need some tools on top
* Need good documentation + structure (several how-to-s, best practices, quick start guides, etc)
* CLI tools: kubectl / helm / drone / docker / stern / minikube

Experience: Minikube
* Allow to run kubernetes locally
* VirtualBox or xhyve [20] for MacOS to run docker
* Bug with DNS for xhyve (dnsmasq?) and others [24], we suggest VirtualBox
* Run Virtual Env + Docker to run your small Image!

CI
* Concourse: very reach functionality, but not stable, poor documentation, problems with upgrade to v3
* Drone.io: small, concise, fit us well [21]
* Every pipeline stage works in Docker Image
* Not very well documented, sometimes need to read code
* We configured deploy to admin/stage cluster
* Have plugin system

Experience: Geodesic [11]
* Will possibly use soon
* They have similar design
* Very clean implementation

Google evaluation
* “Best Practices”
* Multiple clusters -> good choice
* One large cluster [22] won’t work in the real world
* Need to know Geo loc; Routing based on Geo; Global router (+resilience)
* Service Mesh might help

Current problems
* Naming scheme has some problems (TODO: example with tld)
* Large image -> slow download
* Large image -> slow work (even if image is on host). (FS?)
* We have already 3 ways to install different k8s tools :)


Summary: Cons 1
* Large stack to study (not only technology, but also new concepts)
* Very verbose configs (k8s/helm)
* Some applications are more difficult to run in k8s than in “classical” infrastructure
* Kubernetes will be only a [small] part of your infrastructure
* Still, all current solution on market are too raw

Summary: Cons 2
* All current ‘package managers’ are far from ‘perfect state’
* K8s + Docker-way changes your development habits (2x)
* A lot of tradeoffs to choose creates negative impact
* To run k8s locally you have to make some efforts

Summary: Pros 1
* No need to learn new stack as k8s widely spreads [we hope]
* Release cycle is very short. Commit -> CI -> Image -> Push button to release
* Separation of infra- and business- code
* Very large and active community, a lot of changes (kops, helm, stern, geodesic, rbac, autoscaler, ... - during last 2 years)
* Application + k8s events both are in one place (Kibana)
* No direct access to instances (large class of problems is gone)

Summary: Pros 2
* No @infra help or support for other teams is needed for releases + ‘prod’ issues investigations
* @infra is not a bottleneck anymore, just an “Operating System” for other teams (env + quotes + limits)
* Easy to add error budget: too many errors -> no releases (already in prod) Namespaces, RBAC reduce teams influence
* @infra is not a “Police Department” anymore (common goal instead of “you don’t let us release”)
* Reduced stress and tension in the company

References: part1
1. Continuous Delivery by Jez Humble, David Farley.
https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912
2. Containers are not VMs.
https://blog.docker.com/2016/03/containers-are-not-vms/
3. Docker Distribution (image registry).
https://github.com/docker/distribution
4. Quay - Image Registry as a Service.
https://quay.io
5. etcd-operator - Manager of etcd cluster atop Kubernetes.
https://github.com/coreos/etcd-operator
6. Dex - OpenID Connect Identity (OIDC) and OAuth 2.0 Provider with Pluggable Connectors.
https://github.com/coreos/dex
7. awsudo - sudo-like utility to manage AWS credentials.
https://github.com/makethunder/awsudo
8. Autoscaling-related components for Kubernetes.
https://github.com/kubernetes/autoscaler/
9. Simon’s cat
https://simonscat.com/
10.Helm: Kubernetes package manager
https://helm.sh/
11.Geodesic: framework to create your own cloud platform
https://github.com/cloudposse/geodesic
12.Calico: Configuring IP-in-IP
https://docs.projectcalico.org/v2.2/usage/configuration/ip-in-ip

References: part2

13.Sensu: Open-core monitoring platform
https://github.com/sensu/sensu
14.InfluxDB: Scalable datastore for metrics, events, and real-time analytics
https://github.com/influxdata/influxdb
15.Cernan: Telemetry and logging aggregation server
https://github.com/postmates/cernan
16.Prometheus: Open Source monitoring solution
https://prometheus.io/
17.Heapster: Compute Resource Usage Analysis and Monitoring of Container Clusters
https://github.com/kubernetes/heapster
18.Stern: Multi pod and container log tailing for Kubernetes
https://github.com/wercker/stern
19.Minikube: tool to run Kubernetes locally
https://github.com/kubernetes/minikube
20.Docker machine driver fox xhyve native OS X Hypervisor
https://github.com/zchee/docker-machine-driver-xhyve
21.Drone: Continuous Delivery platform built on Docker, written in Go
https://github.com/drone/drone
22.Borg, Omega and Kubernetes
http://queue.acm.org/detail.cfm?id=2898444
23.Container-Native Networking - Comparison
https://docs.google.com/spreadsheets/d/1polIS2pvjOxCZ7hpXbra68CluwOZybsP1IYfr-HrAXc/edit#gid=0
24.Bug in minikube when working with xhyve driver
https://github.com/kubernetes/minikube/issues/1442


## Links
[RU] [Video] [slurm.io](https://www.youtube.com/channel/UCK5MedKoNJ5aRahfGOIGx6g)
