# Coursera Python Training 2
# Lucas Silva
# Week 1 - Exercício Extra 1 - Imprimindo Matrizes

def imprime_matriz(matriz):
    for i in range(0,len(matriz)):
        #linhas
        for j in range(0,len(matriz[0])):
            #colunas
            if(j==(len(matriz[0])-1)):
                print(matriz[i][j], end="")
            else:
                print(matriz[i][j], end=" ")
        print()