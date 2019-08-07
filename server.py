import ssl
import socket

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('EC.pem','EC.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('127.0.0.1',8443))
    sock.listen(5)
    with context.wrap_socket(sock, server_side = True) as ssock:
        conn, addr = ssock.accept()


#openssl req -new -x509 -days 365 -nodes -out EC.pem -keyout EC.key