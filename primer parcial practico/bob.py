import funciones_rsa
from Crypto.Cipher import DES, AES

password_bob = "bob"


# A Cargar la clave privada de Bob y la clave pública de Alice
key_bob = funciones_rsa.cargar_RSAKey_Privada("Pri_B" + ".pem", password_bob)
key_alice = funciones_rsa.cargar_RSAKey_Publica("Pub_A" + ".pub")

# B Cargar el texto cifrado y la firma digital.
cifrado = open("apartadoC.bin", "rb").read()
firma = open("apartadoD.bin", "rb").read()
textoCifrado=open("apartadoE.bin", "rb").read()
nonce=open("nonce.bin", "rb").read()
mac=open("mac.bin", "rb").read()
# D Descifrar el texto cifrado y mostrarlo por pantalla.
descifrado = funciones_rsa.descifrarRSA_OAEP(cifrado, key_bob)

# C Comprobar la validez de la firma digital.
if funciones_rsa.comprobarRSA_PSS(descifrado, firma, key_alice):
    print("La firma es valida. El mensaje proviene de Alice.")
else:
    print("La firma es INVALIDA. El mensaje NO proviene de Alice.")

# E y F Descifrar el texto  y mostrarlo 
print("clave descifrada: " + descifrado)
try:
    aes_descifrado = AES.new(bytes(descifrado, 'utf-8'), AES.MODE_GCM, nonce )
    datos_claro = aes_descifrado.decrypt_and_verify(textoCifrado, mac).decode("utf-8", "ignore")
    print(datos_claro)
except (ValueError, KeyError) as e:
    print("Error en el descifrado de AES GCM")
