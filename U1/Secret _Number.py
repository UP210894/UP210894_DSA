import os
from random import randrange

numero = 0
secreto = randrange (0, 11 )

menor = 0
mayor = 10
os.system ("cls")

while (numero != secreto):
    print(menor, "<----------->", mayor)

    numero = int(input("Ingresa un número del 1 al 100:  "))
    os.system ("cls")
    if (numero < secreto):
        menor = numero
        print ("Subele")
    elif (numero > secreto):
        mayor = numero
        print ("Bajale")
    else:
        continue

print("Ganaste")