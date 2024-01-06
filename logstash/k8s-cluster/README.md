Start our k8s cluster using minikube and mounting this directory into minikube:

```bash
minikube start \
    --driver=docker \
    --mount-string="$(pwd)/logstash:/data" --mount

# then mount fs
minikube mount $(pwd)/logstash:/data
```


First create the ConfigMap, which defines the contents of both `logstash.yml` and `pipelines.yml`.
Then apply it using:

```bash
kubectl apply -f config_map.yaml
```

Then create the Logstash Pods deployment set:


```bash
kubectl apply -f deployment.yaml
```
