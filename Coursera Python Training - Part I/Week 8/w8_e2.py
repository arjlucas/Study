# Coursera Python Training 1
# Lucas Silva
# Week 8 - Exercício 2 - Soma dos Elementos da Lista

def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = sum(lista)
    return soma

lista=[1,2,3,4,5]
print(soma_elementos(lista))