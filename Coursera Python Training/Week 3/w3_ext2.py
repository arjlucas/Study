# Coursera Python Training 1
# Lucas Silva
# Week 3 - Exercício Extra 2 - Bháskara

import math
a = float(input("Insira o valor do elemento A:"))
b = float(input("Insira o valor do elemento B:"))
c = float(input("Insira o valor do elemento C:"))
delta = ((b**2) - (4*a*c))
if delta < 0:
    print ("esta equação não possui raízes reais")
elif delta == 0:
    raiz = (-b + (math.sqrt(delta))) / (2 * a)
    print ("a raiz desta equação é", raiz)
elif delta > 0:
    raiz1 = (-b + (math.sqrt(delta))) / (2 * a)
    raiz2 = (-b - (math.sqrt(delta))) / (2 * a)
    if raiz1<raiz2:
        print ("as raízes da equação são", raiz1,"e", raiz2)
    else:
        print("as raízes da equação são", raiz2, "e", raiz1)