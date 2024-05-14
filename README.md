# ITDS project

## How to build and run the project

```bash
docker-compose up --build
```

## Build and push to Docker hub

```bash
docker build --platform=linux/amd64 -t serart/itds .
docker push serart/itds
```
