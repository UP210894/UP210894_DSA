import math as ma

x1 = 1
x2 = 2
xm = None
Es = 0.001 
Er = abs(x2-x1)    
i = 1
it = round((ma.log(x2 - x1) - ma.log(Es)) / ma.log(2))
print('Iterations: ',it)

print('i','x1','x2','Er','xm','f(x1)','f(xm)','f(x1) * f(xm)',sep='\t|')

while (Er >= Es):
        xm = (x1 + x2) / 2
        print (i, round(x1,3),round(x2,3),round(Er,3),round(xm,3),round(((x1 ** 2) - 2),3),round(((xm ** 2) - 2),3), round((round(((x1 ** 2) - 2),3))*(round(((xm ** 2) - 2),3)),3),sep='\t|')
        if (((x1 ** 2) - 2) * ((xm ** 2) - 2) < 0): 
            x2 = xm
        else:
            x1 = xm 
        Er = abs(x2 - x1)
        i = i + 1

print('Root: ',xm)