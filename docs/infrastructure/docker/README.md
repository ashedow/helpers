# Docker

## Tips and tricks for Dockerfile

One process - one container

***

Better use smalest base image. Use tags and versions. Do not use `latest`
```
FROM alpine:3.11.5 
```

***
Don't forget to clear cash
```
RUN apt-get update && apt-get install -u \
nginx \
 && rm -rf /var/lib/apt/lists/*
```

***

Use layer power. 

less strings -> less layers

***

move frequently modified layers to the end of file. Like
```
COPY .  /opt/
ENTRYPOINT[“/bin/project”]
CMD[“--help”]
```

***

## .dockerignore

> Like .gitignore, but .dockerignore

## Cache


