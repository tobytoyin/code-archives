```shell
docker run --rm -it \
    -p 5400:5400 \
    -v $(pwd)/pipeline/:/usr/share/logstash/pipeline/ \
    -v $(pwd)/pipelines.yml:/usr/share/logstash/config/pipelines.yml \
    -v $(pwd)/logstash.yml:/usr/share/logstash/config/logstash.yml \
    docker.elastic.co/logstash/logstash:8.11.1 \
    -f /usr/share/logstash/pipeline/syslog-input.conf
```

Then telnet into it :

```shell
telnet localhost 514
```

Then enter the logs into the terminal.
