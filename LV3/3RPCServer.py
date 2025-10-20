import socket
import threading
import rpyc

brojac = 0

class MyService(rpyc.Service):
    vlasnik = 'Joe'
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass
        
    def exposed_vlasnik(self):
        global brojac
        brojac =+ 1
        return self.vlasnik

    def exposed_promet(self):
        global brojac
        brojac =+ 1
        return brojac
    
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=25555)
    t.start()