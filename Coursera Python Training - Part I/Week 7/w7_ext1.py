# Coursera Python Training 1
# Lucas Silva
# Week 7 - Exercício Extra 1 - Checagem Número de Primos

def n_primos(n):
    cont = 0
    primo = False
    if n >= 2:
        for i in range(2, n + 1):
            div = 0
            for j in range(1, n + 1):
                if (i % j == 0):
                    div += 1
                    if div>2:
                        break
            if div == 2:
                primo = True
                cont+=1
    return cont

n = int(input("Insira o valor de n:"))
print(n_primos(n))