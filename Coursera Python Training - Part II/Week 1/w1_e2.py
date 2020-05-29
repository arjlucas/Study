# Coursera Python Training 2
# Lucas Silva
# Week 1 - Exercício 2 - Soma de Matrizes



def soma_matrizes(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        m3=[]
        for i in range(0,len(m1)):
            linha=[]
            for j in range(0,len(m1[0])):
                linha.append(m1[i][j] + m2[i][j])
            m3.append(linha)
        return m3
    else:
        return False
    
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))