from datetime import datetime
import socket
import threading
import rpyc
import time

minuta = 0

def prva():
    c = rpyc.connect('localhost', 25555)
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    c.root.registriraj(IP, 25556)
    time.sleep(15)

    print("Trenutna minuta: ", c.root.vrijeme())

    c.close()

def druga():
    class MyService(rpyc.Service):
        def on_connect(self, conn):
            pass
        
        def on_disconnect(self, conn):
            pass

        def exposed_minu(self):
            global minuta
            return datetime.now().minute
    
    if __name__ == "__main__":
        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(MyService, port=25556)
        t.start()


t1 = threading.Thread(target=druga, args=())
t2 = threading.Thread(target=prva, args=())
t1.start()
t2.start()
