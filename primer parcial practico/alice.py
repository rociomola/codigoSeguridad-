import funciones_rsa
import salsa20
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES


password_alice = "alice"
#texto necesario para cifrar 
texto = "Hola amigos y amigas de la seguridad"
#Datos necesarios para hacer el cifrado AES
nonce_16 = get_random_bytes(16) 
mac_size = 16                   

# a Cargar la clave privada de Alice y la clave pública de Bob. 
key_alice = funciones_rsa.cargar_RSAKey_Privada("Pri_A" + ".pem", password_alice)
key_bob = funciones_rsa.cargar_RSAKey_Publica("Pub_B" + ".pub")

# b Creamos un objeto de cifrado simetrico AES 128 y despues generamos la clave 
k = get_random_bytes(16)
print("Clave Generada: "+ k.hex() )

# c Cifrar k utilizando la clave de Bob.
cifrado = funciones_rsa.cifrarRSA_OAEP(k.hex(), key_bob)
print("Clave cifrada : " + cifrado.hex())

# d Firmar k utilizando la clave de Alice.
firma = funciones_rsa.firmarRSA_PSS(k.hex() , key_alice)
print("Clave firmada : " + firma.hex())

# e ciframos el texto usando AES con la clave k y el modo GCM
cifrador =  AES.new(k, AES.MODE_GCM, nonce = nonce_16, mac_len = mac_size)
datos_cifrado, mac_cifrado = cifrador.encrypt_and_digest(texto.encode("utf-8"))
print("Texto cifrado : " + datos_cifrado.hex())
# e.1  ciframos el texto usando salsa 20
#cifradoSalsa = salsa20.cifarSalsa(k, texto)

# Guardar en ficheros el apartado e ,c , d, y los datos necesarios para descifrar 
print("Guardando apartado c")
file_cifra = open("apartadoC.bin", "wb")
file_cifra.write(cifrado)
file_cifra.close()

print("Guardando apartado d")
file_cifra = open("apartadoD.bin", "wb")
file_cifra.write(firma)
file_cifra.close()

print("Guardando apartado e")
file_cifra = open("apartadoE.bin", "wb")
file_cifra.write(datos_cifrado)
file_cifra.close()

print("Guardando nonce")
file_cifra = open("nonce.bin", "wb")
file_cifra.write(nonce_16)
file_cifra.close()

print("Guardando mac")
file_cifra = open("mac.bin", "wb")
file_cifra.write(mac_cifrado)
file_cifra.close()
