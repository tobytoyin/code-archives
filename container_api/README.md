## Directories

`backend/` represents an Python API that can be deployed independently
`client/` represents an Python application that use the `backend/` API

## Create the Backend container

At project root `/container_api`, run the following:

```shell
docker compose up --build
```

## Test the API

```shell
curl http://localhost:8080  # source: "backend"
curl http://localhost:8082  # source: "client"
```
