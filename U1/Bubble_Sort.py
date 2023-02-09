arreglo = [58,45,89,56,34,78,56,43,97,23]
ordenado = False
valormayor = None

while (ordenado == False): 
    ordenado = True
    for i in range(len(arreglo)-1):
        if (arreglo[i] > arreglo[i+1]):
            ordenado = False
            valormayor = arreglo[i]
            arreglo[i] = arreglo[i+1]
            arreglo[i + 1] = valormayor

print('Arreglo: ',arreglo)