```shell
docker run --rm -it \
    -v $(pwd)/logstash/pipeline/:/usr/share/logstash/pipeline/ \
    -v $(pwd)/logstash/pipelines.yml:/usr/share/logstash/config/pipelines.yml \
    -v $(pwd)/logstash/logstash.yml:/usr/share/logstash/config/logstash.yml \
    -v $(pwd)/logstash/ruby:/usr/share/logstash/ruby/ \
    docker.elastic.co/logstash/logstash:8.11.1 \
    -f /usr/share/logstash/pipeline/<scriptName>.conf
```
