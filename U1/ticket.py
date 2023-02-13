import random
P=random.randrange(1,1000)
print("El costo de tu ticket es: ",P)

E= int(input("Dime la cantidad a pagar: "))

if(E>P):
    s = E-P
    print("Tu cambio es de: ", s)
else:
    print("TE FALTA VARO CARNAL")

print("-----------------------------------")

H=0
S=int(input("Con cuanto dinero cuentas: "))
while S > H:
    H= H+1
    S= S-1
    S= S-H
print("Te alcanza para ",H," boletos")
print("Te sobra: $ ", S)
