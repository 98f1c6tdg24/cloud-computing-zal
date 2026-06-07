# LAB 2 – Flask container with Docker and Podman

## Docker

```bash
docker build -t flask-cloud-demo .
docker run -d --name flask-docker-demo -p 5000:5000 flask-cloud-demo
```

Open:

```text
http://localhost:5000
```

Cleanup:

```bash
docker rm -f flask-docker-demo
```

## Podman

```bash
podman build -t flask-cloud-demo .
podman run -d --name flask-podman-demo -p 5000:5000 flask-cloud-demo
```

Open:

```text
http://localhost:5000
```

Cleanup:

```bash
podman rm -f flask-podman-demo
```
