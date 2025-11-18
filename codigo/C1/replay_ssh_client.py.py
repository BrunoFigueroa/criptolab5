#!/usr/bin/env python3
# replay_ssh_client.py
# Reproduce el patrón de tráfico (banner + bloques de longitudes similares a la Figura 1).
# USO: python3 replay_ssh_client.py <server_ip> <server_port>
#
import sys, socket, time, os

if len(sys.argv) < 3:
    print("Uso: python3 replay_ssh_client.py <server_ip> <server_port>")
    sys.exit(1)

server = sys.argv[1]
port = int(sys.argv[2])

# Cambia ésta a la versión resaltada en azul en la figura
CLIENT_BANNER = b"SSH-2.0-OpenSSH_7.6p1\r\n"

# Paquetes en orden (basado en tu Figura 1)
# Nota: aquí los valores representan el tamaño aproximado del payload que el cliente enviaría.
# Ajusta longitudes si quieres reproducir exactamente el frame.len que registraste.
payloads = [
    b"",                     # SYN/ACK/handshake manejado por TCP (no enviar)
    CLIENT_BANNER,           # Client banner (ASCII)
    os.urandom(1578),        # Client: Key Exchange Init (random payload del tamaño mostrado)
    os.urandom(114),         # Client: ECDH Key Exchange message (pk)
    os.urandom(82),          # Client: NEWKEYS (mensaje pequeño)
    os.urandom(110),         # Encrypted packet (len=44)
    os.urandom(126),         # Encrypted packet (len=60)
    os.urandom(150),         # Encrypted packet (len=84)
    os.urandom(178),         # Encrypted packet (len=112)
]

# Conectar y enviar en orden, respetando pausas para simular el timing observado.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
print("Conectando a {}:{} ...".format(server, port))
s.connect((server, port))

# leer banner del server (si lo envía)
try:
    srv_banner = s.recv(4096)
    print("Server banner ({} bytes):".format(len(srv_banner)), srv_banner[:120])
except Exception as e:
    print("No recibí banner del server (timeout o cerrado):", e)

# Enviar secuencia de payloads simulados con pequeñas pausas
for i, p in enumerate(payloads):
    if not p:
        continue
    s.sendall(p)
    print("Enviado bloque #{} ({} bytes)".format(i+1, len(p)))
    time.sleep(0.25)   # pausa corta para separar paquetes; ajusta si quieres
# esperar un poco y cerrar
time.sleep(0.5)
s.close()
print("Conexión cerrada.")
