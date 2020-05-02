# Coursera Python Training 1
# Lucas Silva
# Week 4 - Exercício 1 - Fatorial de N

n=int(input("Insira o valor de n:"))
i=n
fat=1
if n!=0:
    while i>1:
        fat = fat * i
        i-=1
print(fat)