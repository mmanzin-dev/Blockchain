import os
import binascii
import hashlib
from ecdsa import SigningKey, SECP256k1
import ecdsa
import base58

#na temelju privatnog ključa stvara javni ključ
def privatni_u_javni(prkey):
    private_key_bytes = bytes.fromhex(prkey)
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    vk = sk.get_verifying_key()
    public_key_hex = vk.to_string("uncompressed").hex()
    return public_key_hex

#na temelju javnog ključa stvara bitcoin adresu
def javni_u_adresu(pukey):
    public_key_bytes = bytes.fromhex(pukey)
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(public_key_bytes).digest())
    hash160 = ripemd160.digest()
    network_byte = b'\x00'  # Mainnet address starts with '1'
    address_bytes = network_byte + hash160
    checksum = hashlib.sha256(hashlib.sha256(address_bytes).digest()).digest()[:4]
    address_with_checksum = address_bytes + checksum
    bitcoin_address = base58.b58encode(address_with_checksum).decode('utf-8')
    return bitcoin_address

#stvara nasumičan privatan ključ
def generate_private_key():
    private_key = os.urandom(32)
    return binascii.hexlify(private_key).decode('utf-8')

#iz datoteke novčanici.dat dohvaća popis stvorenih novčanika
def dohvati_novcanike():
    try:
        nov = open("novcanici.dat", "r")
        popis_nov = nov.readlines()
        nov.close()
        return popis_nov
    except:
        return False

#stvara novi novčanik tako da njegovo ime dodaje u datoteku novčanici.dat
def stvori_novcanik(ime):
    nov = open("novcanici.dat", "a")
    nov.write(ime+"\n")
    nov.close()
    return True

#Poziva generiranje novog ključa i dodaje ga u datoteku novčanika
#svaki novčanik ima svoju .dat datoteku u obliku ime_novčanika.dat
def dodaj_kljuc(novcanik):
    nov = open(novcanik+".dat", "a")
    nov.write(generate_private_key()+"\n")
    nov.close()
    return True

#svaki novčanik ima svoju .dat datoteku u obliku ime_novčanika.dat
#u navedenoj datoteci se nalaze privatni ključevi novčanika
def dohvati_kljuceve(ime):
    try:
        nov = open(ime+".dat", "r")
        kljucevi = nov.readlines()
        nov.close()
        return kljucevi
    except:
        return False

#korištenjem privatnog ključa stvara digitalni potpis poruke
def stvori_potpis(poruka, prkljuc):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(prkljuc), curve=ecdsa.SECP256k1)
    poruka = poruka.encode()
    # Sign the message using the private key
    signature = sk.sign(poruka)
    # Convert the signature to its hexadecimal representation
    signature_hex = signature.hex()
    return signature_hex

#provjerava da li digitalni potpis odgovara primljenoj poruci
#pri tom je potrebno dostaviti u javni ključ koji odgovara privatnom ključu koji je izradio digitalni potpis
def provjeri_potpis(poruka,potpis,pukey):
    # Parse the public key and signature from their hexadecimal representations
    public_key = ecdsa.VerifyingKey.from_string(bytes.fromhex(pukey), curve=ecdsa.SECP256k1)
    signature = bytes.fromhex(potpis)
    poruka = poruka.encode()
    try:
        # Verify the signature
        if public_key.verify(signature, poruka):
            print("Potpis je valjan!")
            return True
        else:
            print("Potpis nije valjan!")
            return False
    except ecdsa.keys.BadSignatureError:
        print("Potpis nije valjan!")
        return False

