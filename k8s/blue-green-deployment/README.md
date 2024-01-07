## Setting up the Service

First start by creating a Service of our "application".
This service would be selecting the "blue version" Pods using `version=blue` label initially.

```bash
kubectl apply -f app-service.yaml
```

## Deploying the "blue" vesion

First start by building the blue version nginx image, then push it to minikube registry:

```bash
podman build -f docker/dockerfile --build-arg INDEX_PAGE="index-blue.html" -t nginx:blue
```

Then apply the "blue version" deployment:

```bash
kubectl apply -f blue-deployment.yaml
```

Then we check that our service is routing to the "blue version" webpage. We first open another termainl to port-forward the
clusterIP and nginx port to localhost:

```bash
kubectl port-forward services/app-service 8080:80
```

Then check the nginx home page:

```bash
curl http://localhost:8080
# > Blue Version of Nginx
```

## Deploying the "green" version and update the service

First starting by build the green version of the nginx image, then push it to minikube registry.

```bash
podman build -f docker/dockerfile --build-arg INDEX_PAGE="index-green.html" -t nginx:green
```

Then apply the "green version" deployment:

```bash
kubectl apply -f green-deployment.yaml
```

If we check the localhost at this point, it would still be the "blue version" index page. Since we haven't updated the service to route traffics
to the "green version" yet:

```bash
curl http://localhost:8080
# > Blue Version of Nginx
```

We can update the Service to route traffics to the "green-deployment" by directly editting the Service and
change `selector.version=green`:

```bash
kubectl edit svc app-service
```

Wait a while for the update to complete and then check it again:

```bash
curl http://localhost:8080
# > Green Version of Nginx
```

## Cleanup Blue Deployment

In most cases, the two services (blue & green app-service routing) would be running in parallel with a weighted load balancing.
For this example, we just delete the `blue-deployment` once we confirm the `green-deployment` is working.

```bash
kubectl delete deployments blue-deployment
kubectl get deployments
```
