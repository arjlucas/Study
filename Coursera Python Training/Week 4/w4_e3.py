# Coursera Python Training 1
# Lucas Silva
# Week 4 - Exercício 3 - Soma dos Dígitos de N

n=int(input("Insira o valor de n:"))
tam=len(str(n))
i=tam
soma=0
while i>=1:
    soma = soma + (n % (10 ** i) // 10 ** (i - 1))
    i-=1
print(soma)