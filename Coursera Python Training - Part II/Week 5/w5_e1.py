# Coursera Python Training 2
# Lucas Silva
# Week 5 - Exercício 1 - Busca Binária

def busca(lista, elemento):
    first = 0
    last = len(lista)- 1
    
    while first<=last:
        mid = (first+last)//2
        print(mid)
        if lista[mid] == elemento:
            return mid
        else:
            if elemento < lista[mid]:
                last = mid - 1
            else:
                first = mid +1
    return False
