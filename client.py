import ssl
import socket

hostname = '127.0.0.1'
context = ssl._create_unverified_context()

with socket.create_connection((hostname, 8443)) as sock:
    with context.wrap_socket(sock, server_hostname = hostname) as ssock:
        print(ssock.version())
