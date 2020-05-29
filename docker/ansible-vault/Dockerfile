FROM alpine:3.8
# FROM ubuntu:eoan

# ARG ANSIBLE_VERSION=2.8.0
ENV ANSIBLE_VERSION=2.9.0

# RUN apt-get update && apt-get install --yes --no-install-recommends \
#   ansible=${ANSIBLE_VERSION} \
# && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN set -x && apk update && apk upgrade && \
    apk --update add --virtual build-dependencies \
        gcc \
        musl-dev \
        python3 \
        bash \
        libffi-dev \
        openssl-dev \
        python3-dev \
        make && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache && \
    pip3 install ansible==${ANSIBLE_VERSION} cryptography==2.5 pycrypto==2.6.1 && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /etc/ansible /ansible

ENTRYPOINT ["ansible-vault"]
CMD ["--help"]
HEALTHCHECK NONE
