precio = 0
dinero = int (input("Ingresa la cantidad de dinero: "))

while (dinero > precio):
    precio += 1
    dinero -= precio
    
print("Cantidad de boletos: ", precio)