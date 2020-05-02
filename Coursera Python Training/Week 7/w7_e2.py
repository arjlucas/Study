# Exercícios Week 7 - Coursera Python Training 1
# Lucas Silva

l = int(input("digite a largura:"))
a = int(input("digite a altura:"))

for i in range(1,a+1):
    for j in range(1,l+1):
        if (i>1) and (i<a) and (j>1) and (j<l):
            print(" ", end="")
        else:
            print("#", end="")
    print()