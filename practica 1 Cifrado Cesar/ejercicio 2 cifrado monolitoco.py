def cifradoMonoalfabetico(cadena, clave):
    resultado = ''
    i = 0
    c = 0

    while i < len(cadena):
        ordReal= ord(cadena[i])
        ordClave = ord(clave[c])
        ordCifrado = 0

        if (ordReal >= 97 and ordReal <= 122 and ordClave >= 97 and ordClave <= 122):
            ordCifrado = (((ordReal - 97) - ((ordClave - 97 ) + 1)) % 26) + 97
        
        if (ordReal >= 65 and ordReal <= 90 and ordClave >= 65 and ordClave <= 90):
            ordCifrado = (((ordReal - 65) - ((ordClave - 65 ) + 1)) % 26) + 65
        
        resultado = resultado + chr(ordCifrado)

        i = i + 1
        c = c + 1

        if(c > len(clave)-1):
            c = 0
    return resultado
print("----------------------------------------")
print("Ejercicio 2: cifrado monolitico")
print("----------------------------------------")
cadena = input("Escriba su texto a cifrar (recomendamos que solo use mayusculas o munusculas durante todo el proceso): ")
clave = input("Escriba su palabra clave (recomendamos que solo use mayusculas o munusculas durante todo el proceso): ")
print("----------------------------------------")
print(cadena)
cadena = cifradoMonoalfabetico(cadena, clave) 
print(cadena)
print("----------------------------------------")
