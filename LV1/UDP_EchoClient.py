import socket

HOST = "127.0.0.1"
PORT = 64444

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello network", (HOST, PORT))
    data = s.recv(1024)

print("Received", data)