def cifradoCesarAlfabetoInglesMAY(cadena,desplazamiento):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + desplazamiento) % 26) + 65
        else:
            if (ordenClaro >= 97 and ordenClaro <= 122): #Apartado B
                ordenCifrado = (((ordenClaro - 97) + desplazamiento) % 26) + 97
        
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado
def descifradoCesarAlfabetoInglesMAY(cadena, desplazamiento):
    """Devuelve un descifrado Cesar tradicional (+desplazamiento)"""
    # Definir la nueva cadena resultado
    resultado = ''
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Añade el caracter cifrado al resultado
        if (ordenClaro >= 65 and ordenClaro <= 90): #Apartado A
            ordenCifrado = (((ordenClaro - 65) - desplazamiento) % 26) + 65
        else:
            if (ordenClaro >= 97 and ordenClaro <= 122): #Apartado B
                ordenCifrado = (((ordenClaro - 97) - desplazamiento) % 26) + 97
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    return resultado


print("----------------------------------------")
teclado=input("Escriba el desplazamiento selecionado en numero entero sin decimales: ")
desplazamiento = int(teclado) #Apartado C
print("----------------------------------------")
print("PRACTICA 1. SEGURIDAD DE LA INFORMACIÓN")
print("----------------------------------------")
claroCESAR = input("Escriba el texto a cifrar: ")
print(claroCESAR)
cifradoCESAR = cifradoCesarAlfabetoInglesMAY(claroCESAR, desplazamiento) #Añadir J ---> Apartado C
print(cifradoCESAR)
print("----------------------------------------")
cifradoCESAR =input("Escriba el texto a descifrar: ")
print(cifradoCESAR)
descifradoCESAR = descifradoCesarAlfabetoInglesMAY(cifradoCESAR, desplazamiento) #Añadir J ---> Apartado C
print(descifradoCESAR)
print("----------------------------------------")