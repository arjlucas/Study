# Coursera Python Training 1
# Lucas Silva
# Week 4 - Exercício 2 - N primeiros números ímpares naturais

n=int(input("Insira o valor de n:"))
i=1
c=0
while i<=10 and c<=n:
    if i%2!=0:
        print(i)
        c+=1
    i+=1