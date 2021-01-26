# Docker

## Tips and tricks for Dockerfile

One process - one container

***

Better use smalest base image. Use tags and versions. Do not use `latest`
```
FROM alpine:3.11.5 
```

***

*Multistage builds* are useful to anyone who has struggled to optimize Dockerfiles while keeping them easy to read and maintain.
> https://docs.docker.com/develop/develop-images/multistage-build/

use multiple FROM statements in your Dockerfile. Each FROM instruction can use a different base, and each of them begins a new stage of the build. You can selectively copy artifacts from one stage to another, leaving behind everything you don’t want in the final image. To show how this works, let’s adapt the Dockerfile from the previous section to use multi-stage builds.

```
FROM golang:1.7.3 AS builder
WORKDIR /go/src/github.com/alexellis/href-counter/
RUN go get -d -v golang.org/x/net/html  
COPY app.go    .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /go/src/github.com/alexellis/href-counter/app .
CMD ["./app"] 
```

And `$ docker build --target builder -t alexellis2/href-counter:latest .`

***

Use a previous stage as a new stage
You can pick up where a previous stage left off by referring to it when using the FROM directive. For example:
```
FROM alpine:latest as builder
RUN apk --no-cache add build-base

FROM builder as build1
COPY source1.cpp source.cpp
RUN g++ -o /binary source.cpp

FROM builder as build2
COPY source2.cpp source.cpp
RUN g++ -o /binary source.cpp
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


## Do not use root!


```python
import os, socket, pwd
HOST, PORT = '', 90

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    user = pwd.getpwnam('nobody')
    os.setgid(arguments.user.pw_gid) # first change group
    os.setuid(arguments.user.pw_uid)
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            conn.sendall(data)
```

