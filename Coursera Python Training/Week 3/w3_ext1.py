# Coursera Python Training 1
# Lucas Silva
# Week 3 - Exercício Extra 1 - Distância entre dois pontos.

import math
x1=float(input("Insira x1:"))
x2=float(input("Insira x2:"))
y1=float(input("Insira y1:"))
y2=float(input("Insira y2:"))
d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
if d>=10:
    print("longe")
else:
    print("perto")