import random
 
def matriz6x6():
    return random.sample(range(1,100), 36)
 
result=matriz6x6()
for i in range(0, len(result), 6):
    print(result[i:i+6])

#NOTA: ES UNA MATRIZ SENCILLA 