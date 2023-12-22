`sample/sample-log.json` is a sample DCR log for the sentinel table.

Since we need to install extra sentinel, an extra `dockerfile` is created ontop of existing Logstash office image. This `dockerfile` include additional steps, including:
1. install required azure logstash plugins
2. create logstash keystore (in `add_keystore.sh`)
3. load `.env.dev` files and populate secrets into logstash keystore (in `add_keystore.sh`)

To use this container, first build it
```shell
# using docker
docker build -t logstash-stnl docker/

# or using podman
podman machine set --rootful
podman machine start
podman build -f dockerfile -t logstash-stnl docker/
```

Then run it as container job, where `{JobName}` can be:
- `write-to-custom-table.conf`
- `write-to-standard-table.conf`

```shell
podman run --rm -it \
    -v $(pwd)/pipeline/:/usr/share/logstash/pipeline/ \
    -v $(pwd)/pipelines.yml:/usr/share/logstash/config/pipelines.yml \
    -v $(pwd)/logstash.yml:/usr/share/logstash/config/logstash.yml \
    logstash-stnl \
    -f /usr/share/logstash/pipeline/{JobName}
```
