# Coursera Python Training 1
# Lucas Silva
# Week 8 - Exercício 1 - Removendo elementos repetidos

def remove_repetidos(lista):
    lista = sorted(set(lista))
    return lista

lista = [1,2,4,2,6,4,5,8,1,7]
print(remove_repetidos(lista))
