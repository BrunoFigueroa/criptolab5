# Dockerfile C3
ARG UBUNTU_VERSION=20.10
FROM ubuntu:${UBUNTU_VERSION}

ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g' /etc/apt/sources.list \
 && sed -i 's|http://security.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g' /etc/apt/sources.list


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      openssh-client \
      ca-certificates \
      iproute2 \
      iputils-ping \
      net-tools \
      tcpdump \
      vim \
      less \
      busybox \
      sshpass || true

CMD ["sleep", "infinity"]
