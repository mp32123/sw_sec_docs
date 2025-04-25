* How to deploy this app to DockerHub

```
docker build -t latest .
docker tag tomerikroos/webapp-hydra:latest tomerikroos/webapp-hydra:latest
docker push tomerikroos/webapp-hydra:latest
```