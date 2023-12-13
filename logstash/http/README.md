```shell
docker run --rm -it \
    -p 8080:8080 \
    -v $(pwd)/pipeline/:/usr/share/logstash/pipeline/ \
    -v $(pwd)/pipelines.yml:/usr/share/logstash/config/pipelines.yml \
    -v $(pwd)/logstash.yml:/usr/share/logstash/config/logstash.yml \
    docker.elastic.co/logstash/logstash:8.11.1 \
    -f /usr/share/logstash/pipeline/push-pattern-post.conf
```

We can post a simple JSON by using Postman or `curl`

```shell
curl -X POST -H "Content-Type: application/json" -d '{"key1":"value1", "key2":"value2"}' http://localhost:8080

```

Then enter the logs into the terminal.
