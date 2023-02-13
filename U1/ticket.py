import random
P=random.randrange(1,1000)
print("El costo de tu ticket es: ",P)

E= int(input("Dime la cantidad a pagar: "))

if(E>P):
    s = E-P
    print("Tu cambio es de: ", s)
else:
    print("TE FALTA VARO CARNAL")
