import socket  #uvoz modula socket

HOST = '127.0.0.1'    # varijabla s pridruženom IP adresom (localhost) 
PORT = 22244	      # varijabla s pridruženim mrežnim portom

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    s.setblocking(False)

    while True:
        try:
            conn, addr = s.accept()
        except:
            continue

        with conn:
            print('Connected by', addr)
            while True:
                try:
                    data = conn.recv(1024)
                except:
                    continue

                if not data:
                    break
                conn.sendall(data)
