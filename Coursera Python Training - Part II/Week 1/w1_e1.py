# Coursera Python Training 2
# Lucas Silva
# Week 1 - Exercício 1 - Dimensões de uma Matriz

def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    print(f"{linhas}X{colunas}")
    
minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)