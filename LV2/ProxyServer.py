import socket

HOST = "127.0.0.1"
PORT = 63444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)

            while True:
                data = conn.recv(1024)
                data = data + b"#PS#"

                if not data:
                    break

                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s1:
                    s1.sendto(data,("localhost", 44555))
                    data = s1.recv(1024)
                    print("Primljeno s UDP echo servera")

                data = data + b"#PS#"
                conn.sendall(data)

        answer = input("Continue running the server? [Y/N]: ")
        if answer.upper() == "N":
            break