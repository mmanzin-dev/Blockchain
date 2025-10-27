import os
import binascii
import hashlib
import ecdsa
import base58
from ecdsa import SigningKey, SECP256k1
from funkcije import *

novcanik = None

while True:
    print(f"""

    ******************************************
    Učitani novčanik:   {novcanik}
    ******************************************""")
    akc = int(input("""Odaberi akciju:
    1-Učitaj novčanik
    2-Stvori novi novčanik
    3-Dodaj privatni ključ u novčanik
    4-Prikaži adrese u novčaniku
    5-Stvori potpis
    6-Provjeri potpis
    7-Prekini program
    Odabir[1-7]:"""))


    if akc == 1:
        # Dohvatiti popis novčanika iz datoteke i omogućiti korisniku da odabere novčanik s kojim će raditi
        # Ime odabranog novčanika pridružiti varijabli novcanik koja je inicijalno postavljena u None
        popis=dohvati_novcanike()
        if popis==False:
            print("Potrebno je stvoriti novi novčanik!")
        else:
            brojac=1
            for i in popis:
                print(f"[{brojac}]",i.rstrip('\n'),end="   ")
                brojac+=1
            odabir=int(input("\nUnesi broj novčanika koji želite učitati: "))
            novcanik=popis[odabir-1]
            novcanik=novcanik.rstrip('\n')

    elif akc == 2:
        # Omogućiti korisniku da unese ime novog novčanika
        ime = input("Unesite naziv novog novcanika: ")

        # Zatim iskoristiti odgovarajuću funkciju za stvaranje novog novčanika
        if stvori_novcanik(ime):
            print("Novcanik stvoren")
    elif akc == 3:
        # Provjeriti da li je korisnik odabrao novčanik. Ako je, iskoristiti odgovarajuću funkciju za dodavanje novog ključa u novčanik
        if novcanik != None:
            if (dodaj_kljuc(novcanik)):
                print("Privatni kljuc stvoren")
            else:
                print("Novacnik nije odabran")

    elif akc == 4:
        # Provjeriti da li je korisnik odabrao novčanik. Ako je, ispisati sve Bitcoin adrese pridružene novčaniku
        if novcanik != None:
            kljucevi = dohvati_kljuceve(novcanik)

            # Bitcoin adrese se računaju na temelju javnog ključa, dok se javni ključ računa na temelju privatnog koji je pohranjen u datoteci novčanika
            for kljuc in kljucevi:
                print("Adresa: ", javni_u_adresu(privatni_u_javni(kljuc)))
        else:
            print("Novcanik nije odabran")

    elif akc == 5:
        # Provjeriti da li je korisnik odabrao novčanik. Ako je, učitati prvi privatni ključ iz datoteke novčanika.
        if novcanik != None:
            kljucevi = dohvati_kljuceve(novcanik)

            if kljucevi == False:
                print("Nema kljuceva")
            else:
                kljuc = kljucevi[0]
                # Zatim korisnika tražiti da upiše poruku koju želi digitalno potpisati. Spremiti poruku u odgovarajuću varijablu.
                poruka = input("Unesite poruku za potpis: ")

                # Stvoriti digitalni potpis poruke te na kraju ispisati poruku, potpis i javni ključ koji se može kasnije iskoristiti za provjeru potpisa
                digitalni_potpis = stvori_potpis(poruka, kljuc)
                print("Poruka: ", poruka)
                print("DIgitalni potpis: ", digitalni_potpis)
                print("Javni kljuc: ", privatni_u_javni(kljuc))
        else:
            print("Novcanik nije odabran")

    elif akc == 6:
        # Korisnika tražiti da unese poruku, digitalni potpis i javni ključ te zatim pomoću odgovarajuće funkcije napraviti provjeru poruke i digitalnog potpisa
        if novcanik != None:
            poruka = input("Unesite poruku: ")
            digitalni_potpis = input("Unesite digitalni potpis: ")
            javni_kljuc = input("Unesite javni kljuc: ")

            provjereni_potpis = provjeri_potpis(poruka, digitalni_potpis, javni_kljuc)
            print("Rezultat provjerenog potpisa: ", provjereni_potpis)
        else:
            print("Novcanik nije odabran")

    elif akc == 7:
        break