#!/bin/bash

# Generar host keys si no existen
if [ ! -f /etc/ssh/ssh_host_rsa_key ]; then
  ssh-keygen -A
fi

# Asegura que PasswordAuthentication esté habilitado
if grep -q "^PasswordAuthentication" /etc/ssh/sshd_config; then
  sed -i 's/^PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
else
  echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
fi

# Bloquear root
if grep -q "^PermitRootLogin" /etc/ssh/sshd_config; then
  sed -i 's/^PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
else
  echo "PermitRootLogin no" >> /etc/ssh/sshd_config
fi

# Asegurar permisos correctos en /var/run/sshd
mkdir -p /var/run/sshd
chmod 755 /var/run/sshd

# Ejecutar servidor SSH
exec /usr/sbin/sshd -D -e
