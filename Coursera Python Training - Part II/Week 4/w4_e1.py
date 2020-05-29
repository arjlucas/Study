# Coursera Python Training 2
# Lucas Silva
# Week 4 - Exercício 1 - Lista Ordenada

def ordenada(lista):
    lista_cp = lista[:]
    lista_cp.sort()
    if lista == lista_cp:
        return True
    else:
        return False
