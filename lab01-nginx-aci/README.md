# LAB 1 – Nginx container with Docker, Podman and Azure Container Instances

## Docker

```bash
docker pull nginx:alpine
docker run -d --name nginx-docker-demo -p 8080:80 nginx:alpine
```

Open:

```text
http://localhost:8080
```

Cleanup:

```bash
docker rm -f nginx-docker-demo
```

## Podman

```bash
podman pull nginx:alpine
podman run -d --name nginx-podman-demo -p 8080:80 nginx:alpine
```

Open:

```text
http://localhost:8080
```

Cleanup:

```bash
podman rm -f nginx-podman-demo
```

## Azure Container Instances

```bash
az group create --name lab-containers-rg --location westeurope

az container create \
  --resource-group lab-containers-rg \
  --name nginx-aci-demo \
  --image nginx:alpine \
  --dns-name-label nginx-aci-demo-$RANDOM \
  --ports 80 \
  --ip-address Public
```

Get FQDN:

```bash
az container show \
  --resource-group lab-containers-rg \
  --name nginx-aci-demo \
  --query ipAddress.fqdn \
  --output tsv
```

Cleanup:

```bash
az group delete --name lab-containers-rg --yes --no-wait
```
