n = int(input("Insira o valor de n:"))
i = 1
cdiv = 0
cdivpr = 0
while i <= n:
    if n % i == 0:
        cdiv+=1
        if i == 1 or i == n:
            cdivpr += 1
    i += 1
if cdiv == cdivpr:
    print("primo")
else:
    print("não primo")