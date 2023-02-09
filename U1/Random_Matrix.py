from random import randrange

diferente = True

tamaño = int(input("Ingrese el tamaño de la matriz cuadrada:  "))
rooms = [[0 for r in range(tamaño)] for f in range(tamaño)]

while (diferente == True):
    numeroaleatorio = randrange (1, tamaño**2 + 1)
    for i in range (len (rooms)):
        for j in range (len (rooms)):
            if (numeroaleatorio == rooms[i][j] or rooms[i][j] == 0):
                rooms [i][j] = numeroaleatorio
                break
            else: 
                continue
        if (rooms[i][j] == numeroaleatorio):
            break

    if (rooms[tamaño-1][tamaño-1] == 0):

        diferente = True
    else :
        diferente = False

print('Matriz aleatoria: ',rooms)


























    
