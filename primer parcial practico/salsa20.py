from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes


def crear_SalsaKey():
    key = get_random_bytes(16) 
    return key

def cifarSalsa (key, cadena):
    cipher = Salsa20.new(key)
    msg = cipher.nonce + cipher.encrypt(cadena)
    return msg

def descifrarSalsa(key, datos):
    msg_nonce = datos[:8]
    ciphertext = datos[8:]
    cipher = Salsa20.new(key, nonce=msg_nonce)
    descifrado = cipher.decrypt(ciphertext)

    return descifrado
