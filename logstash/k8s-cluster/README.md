## K8s cluster pre-requisite

Start our k8s cluster using minikube and mounting this directory into minikube:

```bash
minikube start \
    --driver=docker \
    --mount-string="$(pwd)/logstash:/data" --mount

# then mount fs
minikube mount $(pwd)/logstash:/data
```

## K8s cluster Specification

In the `logstash-k8s.yaml`, we are defining three different things:

- `ConfigMap` is used to define the contents of both `logstash.yml` and `pipelines.yml`.
- `Service` is used to define the network that bound multiple logstash containers together and allow each container to be exposed to the assigned ports
- `Deployment` is the pod template that hosting the logstash container. This also includes defining the `mountPath` of different required yaml files; mounting the pipeline `*.conf` files

We can apply it using:

```bash
kubectl apply -f logstash-k8s.yaml
```

## Testing Ingestion

In the `hello-world.conf`, this include a basic TCP 514 listener and print out the event. We can test how K8s manage to route different traffics to the same pipeline at different logstash instance.

Since we are using minikube, we start by creating two terminals and connect to the `NodePort` localhost's port as if there are two separate network traffics send to our logstash cluster:

```bash
# create 2 terminals and each run
minikube ssh

# install telnet if not already there:
sudo apt-get install telnet

# then send network traffics to the nodeport
telnet localhost 30007
```

We then send two separate messages to identify the source

```bash
# in terminal 1
telnet > machine-1

# in terminal 2
telnet > machine-2
```

Then check the stdout of each individual logstash container, we can see that each container has been loadbalanced to handle one traffic from one terminal at a time.
