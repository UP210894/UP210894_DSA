def prioridad (c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c in ['**']:
        return 3
    else:
        return 4

p = ['5','6','2','+','*','12','4','/','-']
p2 = []
value = 0
posicion = 0
B = 0
a = 0

p.append(')')

while (p[posicion] != ')'):

    if p[posicion] in ['+','-','*','/','**','()']:
        if (p[posicion]== '+'):
            B = p2.pop()
            a = p2.pop()
            c = a + B
            p2.append(c)
        elif (p[posicion]== '-'):
            B = p2.pop()
            a = p2.pop()
            c = a - B
            p2.append(c)
        elif (p[posicion]== '*'):
            B = p2.pop()
            a = p2.pop()
            c = a * B
            p2.append(c)
        elif (p[posicion]== '/'):
            B = p2.pop()
            a = p2.pop()
            c = a / B
            p2.append(c)
        else:
            B = p2.pop()
            a = p2.pop()
            c = a ** B
            p2.append(c)
        prioridad(p[posicion])
        print('La prioridad del operador es', p[posicion], ':',prioridad(p[posicion]))

    else:
        p2.append(int(p[posicion]))

    posicion += 1

value = p2[-1]
print('Resultado:', value)




    


       

    
