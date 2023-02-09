#Funcion
#def(declaracion de funcion)  nombre(nombre)  (variabale)(variable)
def ordenar(stack): 
    return len (stack) == 0 

#Declaracion funcion
def double (x):

#Operacion de la funcion
    y = x * 2

#Lo que regresa la funcion
    return y

#LLamdo de la funcion con imprecion, se le agrega el parametro
print (double(10))

#Declaracoin de un arrego
a = [5,2,7,9,3]

#Ciclo for

for i in range (0, len (a)):
    print (a[i])    
#Ejercicio 1
base = 3
altura = 4
print (((base**2)+(altura**2))**(1/2))

#Leer teclado
#Biblioteca de limpiado de pantalla
import os
#Biblioteca para ingresar tiempo
import time

#Formas de ingresar valores
#print ("Dame tu apellido: t")
#lastname = input()

#name = (input("Dame tu nombre"))

#edad = (input("Dame tu edad: "))
#print (type(edad))

horas = 0
minutos = 1
duracion = 2939

horas = horas + ((minutos + duracion) // 60)
#if horas > 24:
 #horas = horas % 24 

minutos = (minutos + duracion) % 60

print ("Son la: ", horas, ":", minutos )

a = 5
b = 6
c = 7
max  = 0

if a > b:
    if a > c:
        a = a
elif a > b:
    if c > a:
        a = c
elif b > a:
    if b > c:
        a = b
elif b > a:
        b = a
print (a)

#Redondeo
print (round(.1555393,3))
print ("%.3f" % .1555393)


#Modulo 3

a = 1 == 1.
print (a)

a = 0
print (a != 0)
 
#Probelma modulo 3; Ifs
'''
year = int(input("¿Cuatos dias tiene el año?: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif (year % 4) != 0:
    print("Common year") 
elif (year % 100) != 0:
    print("Leap year")
elif (year % 400) != 0:
    print("Common year")
else: 
    print("leap year")4



infinito = 1
while infinito == 1:
    print ("K")

'''
'''
n = 1
pesos = int(input("Ingrese el numero de pesos:  "))

   
print (n)
'''

#for con pass, continue, y break 

'''
for i in range (10):
    pass #pasar a la siguiente instruccion
    continue #continuar con el siguiente ciclo
    break #salir del for 

#Examples word whithout vowels

user_name = input("Give a word")
user_name = user_name.upper()
new_word = ""
for letter in user_name:
    if letter not in ("A", "E", "I", "O", "U"):
        new_word += letter
print(new_word)


co = 16
contador = 0

while co != 1:    
        if co % 2 == 0:
            co = co // 2
            print(co)
            contador += 1
        else : 
            co = (co * 3) + 1
            print (co)
            contador += 1


print(contador)

#Ordenamiento de numeros con sort

number = [10,5,7,9,2,8]
number.sort()
print(number)

ordenado = sorted(number)
print(ordenar)

#Tamaño de la cadena

r = len ("hello")
print (r)

#Metodo para sustituir palabras
#result = data.metodo(arg)

name = "Universidad"
r = name.replace("sida", "vih")
print (r)

#Llenar una lista vacia 
my_list = []
suma = 0
for i in range(5):
    my_list.append((i+1)*10)
    suma += my_list[i]
print(my_list)
print(suma)

#Extraer letras del string

nombre = "Universidad Politecnica"
print (nombre[6:10])

#Separar el string en dos string con el split() cada que encuentre espacios

x = nombre.split()
print(x)
print(x[1])


rooms = [[[False for r in range(20)] for f in range(15)]for b in range (3)]

print(rooms)

from random import randrange

lista = [0,0,0,0,0]
verdad = True

while verdad:
     a = randrange (1, 11)

     for i in range (len (lista)):
        if (lista [i] != a):
            lista.append(a) 
            verdad = True
            break
        else :
            verdad = False

print (lista)


#Tarea 
n= int(input("Ingrese el tamaño:  "))

from random import randrange
rooms = [[0 for r in range(n)] for f in range(n)]

i1 = 0
j1 = 0

for i in range(n):
    for  j in range(n):
        a = randrange (1, 11)
        while (i1 <= n):
            while (j1 <= n):
                print (lista)
'''
from random import randrange

hola = True


n = int(input("Ingrese el tamaño:  "))
rooms = [[0 for r in range(n)] for f in range(n)]
print(rooms)

while (hola == True):
    a = randrange (1, n**2 + 1)
    for i in range (len (rooms)):
        for j in range (len (rooms)):
            if (a == rooms[i][j] or rooms[i][j] == 0):
                rooms [i][j] = a
                break
            else: 
                continue
        if (rooms[i][j] == a):
            break

    if (rooms[n-1][n-1] == 0):

        hola = True
    else :
        hola = False

print(rooms)












