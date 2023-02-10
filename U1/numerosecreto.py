import random
P=random.randrange(1,100)
nu=int(input('Dime el número que crees que he elegido: '))
while nu!=P:
    if nu>P:
        nu=int(input('BAJALE PA: '))
    elif nu<P:
        nu=int(input('SUBELE PA: '))
print('Felicidades has adivinado que el número secreto es:',P)

