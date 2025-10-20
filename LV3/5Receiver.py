print("Pošiljatelj - aktivan")
import rpyc

ime = input("Unesite ime: ")
ip = input("Unesite IP adresu odredista: ")
port = 64445

c = rpyc.connect(ip, port)

print("Za izlaz iz aplikacije unesite qq")

while True:
    poruka = input("Unesite poruku: ")

    if poruka == "qq":
        c.close()
        break

    elif poruka == "povijest":
        povijest = c.root.povijest()
        for poruka in povijest:
            print(poruka)

    else:
        c.root.primi(ime, poruka)