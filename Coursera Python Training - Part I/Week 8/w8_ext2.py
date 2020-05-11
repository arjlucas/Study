# Coursera Python Training 1
# Lucas Silva
# Week 8 - Exercício Extra 2 - Invertendo Elementos em uma Lista

lista=[]

n=int(input("Insira um número:"))

while n!=0:
    lista.append(n)
    n=int(input("Insira um número:"))

lista.reverse()
for i in range(len(lista)):
    print(lista[i])


