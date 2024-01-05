First create the ConfigMap, which defines the contents of both `logstash.yml` and `pipelines.yml`.
Then apply it using:

```bash
kubectl apply -f config_map.yaml
```

Then move the `pipeline/` contents to `/tmp/logstash/pipeline` for the K8s the reference

```bash
mkdir -p /tmp/logstash
cp -r logstash/pipeline /tmp/logstash
```
