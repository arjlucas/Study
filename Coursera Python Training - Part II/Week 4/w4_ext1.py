# Coursera Python Training 2
# Lucas Silva
# Week 4 - Exercício Extra 1 - Gerando Listas Grandes

import random

def lista_grande(n):
    lista=[]
    for i in range(n):
        lista.append(random.randint(1,100))
    return lista