```shell
docker run --rm -it \
    -p 514:514 \
    -v $(pwd)/pipeline/:/usr/share/logstash/pipeline/ \
    -v $(pwd)/pipelines.yml:/usr/share/logstash/config/pipelines.yml \
    -v $(pwd)/logstash.yml:/usr/share/logstash/config/logstash.yml \
    docker.elastic.co/logstash/logstash:8.11.1 \
    -f /usr/share/logstash/pipeline/syslog-input.conf
```