import socket  #uvoz modula socket

HOST = '127.0.0.1'    # varijabla s pridruženom IP adresom (localhost) 
PORT = 63455	      # varijabla s pridruženim mrežnim portom

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    s.setblocking(False)

    while True:
        try:
            data, addr = s.recvfrom(1024)
        except:
            continue
        if not data:
            break
        s.sendto(data,addr)