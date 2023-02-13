import math


def Ecuacion(num):
    return pow(num,2) -2 

x1 = 1 
x2 = 2 
xm = 0 
errorEstandar = 0.001 
errorRelativo = abs(x2 - x1) 
i = 1
it =  round((math.log(x2 - x1) - math.log(errorEstandar)) / math.log(2))
print("Selected equation: x^2 - 2")
print("Iterations: ",it)
print("i\t|x1\t|x2\t|er\t|xm\t|f(x1)\t|f(xm)\t|f(x1)*f(xm)")

while errorRelativo >= errorEstandar:
    xm= (x1 + x2) / 2
    print(i,round(x1,3), round(x2,3), round(errorRelativo,3), round(xm,3), round(Ecuacion(x1),3), round(Ecuacion(xm),3), round((Ecuacion(x1)*Ecuacion(xm)),3), sep="\t|")
    if Ecuacion(x1) * Ecuacion(xm) < 0:
        x2 = xm
    else:
        x1 = xm
    errorRelativo= abs (x2-x1)
    i+=1
print("The root is : ", xm)