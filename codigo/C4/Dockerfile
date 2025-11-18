# Dockerfile C4/S1
ARG UBUNTU_VERSION=22.10
FROM ubuntu:${UBUNTU_VERSION}

ENV DEBIAN_FRONTEND=noninteractive

# Repositorios old-releases para kinetic (EOL)
RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g' /etc/apt/sources.list \
 && sed -i 's|http://security.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g' /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssh-server \
        pwgen \
        openssh-client \
        ca-certificates \
        iproute2 \
        iputils-ping \
        net-tools \
        tcpdump \
        vim \
        less \
        busybox && \
    mkdir -p /var/run/sshd

# Script de arranque
COPY start-sshd.sh /usr/local/bin/start-sshd.sh
RUN chmod +x /usr/local/bin/start-sshd.sh

# Usuario "prueba" para acceso SSH
RUN useradd -m -s /bin/bash prueba && echo "prueba:prueba" | chpasswd


CMD ["/usr/local/bin/start-sshd.sh"]
