# Coursera Python Training 2
# Lucas Silva
# Week 5 - Exercício 2 - Bubble Sort

def bubble_sort(lista):
    fim = len(lista)
    for i in range(fim-1, 0 , -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
        print(lista)
    return lista
