frente = 0
atras = -1
palindromo = True

palabra = str(input("Ingresa una palabra o frase:  "))

palabra = palabra.lower()
palabra = palabra.replace(" ", "")
palabra = palabra.replace("á", "a")
palabra = palabra.replace("é", "e")
palabra = palabra.replace("í", "i")
palabra = palabra.replace("ó", "o")
palabra = palabra.replace("ú", "u")

longitud = len(palabra)
longitud = longitud//2

while (frente <= longitud):
    if (palabra[frente] == palabra[atras]):
        pass
    else:
        palindromo = False
        break
    frente += 1
    atras -=1

print('La palabra o frace es un palindromo: ',palindromo)