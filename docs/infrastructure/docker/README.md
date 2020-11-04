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

