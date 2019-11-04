import funciones_rsa

password_alice = "alice"
password_bob = "bob"


# Crear una clave pública y una clave privada RSA de 2048 bits para Alice. Guardar cada clave en un fichero. 
key = funciones_rsa.crear_RSAKey() 
funciones_rsa.guardar_RSAKey_Privada("Pri_A" + ".pem", key, password_alice)
funciones_rsa.guardar_RSAKey_Publica("Pub_A" + ".pub", key)

# Crear una clave pública y una clave privada RSA de 2048 bits para Bob. Guardar cada clave en un fichero.
key = funciones_rsa.crear_RSAKey()
funciones_rsa.guardar_RSAKey_Privada("Pri_B" + ".pem", key, password_bob)
funciones_rsa.guardar_RSAKey_Publica("Pub_B" + ".pub", key)