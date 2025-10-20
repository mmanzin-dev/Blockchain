print("Primatelj - aktivan")

import rpyc

povijest = []

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_primi(self, user, data):
        global povijest
        povijest.append(data)

        print(user + ": " + data)

    def exposed_povijest(self):
        global povijest
        return povijest

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=64445)
    t.start()