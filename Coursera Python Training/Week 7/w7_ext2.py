# Coursera Python Training 1
# Lucas Silva
# Week 7 - Exercício Extra 2 - Soma das Hipotenusas

import math

def soma_hipotenusas(n):
    cont=0
    for i in range(1, n+1):
        if(é_hipotenusa(i)):
            cont+=i
    return cont

def é_hipotenusa(n):
    hipotenusa = False
    #inserir os laços
    for i in range(1,n):
        for j in range(1,n):
            if n==math.sqrt((i**2)+(j**2)):
                hipotenusa = True
                break
    return hipotenusa

n=int(input("Insira o valor de n:"))
print(soma_hipotenusas(n))
