# Coursera Python Training 1
# Lucas Silva
# Week 7 - Exercício 1 - Impressão de Quadrados

x = int(input("digite a largura:"))
y = int(input("digite a altura:"))

for i in range(1,y+1):
    for j in range(1,x+1):
        print("#", end='')
    print()