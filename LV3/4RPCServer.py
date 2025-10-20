import rpyc
import random

members = []

def most_frequent(List):
    return max(set(List), key = List.count)

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_registriraj(self,ip,port):
        global members
        if (ip,port) not in members:
            members.append((ip,port))
        print(members)

    def exposed_vrijeme(self):
        global members
        minute=[]
        for i in members:
            try:
                c = rpyc.connect(i[0], i[1])
                minute.append(c.root.minu())
            except:
                continue
            c.close()
        print("Trenutna minuta:", minute)
        return most_frequent(minute)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=25555)
    t.start()