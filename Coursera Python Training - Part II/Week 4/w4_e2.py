# Coursera Python Training 2
# Lucas Silva
# Week 4 - Exercício 1 - Lista Ordenada
    
def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False
