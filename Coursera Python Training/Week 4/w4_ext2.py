n=int(input("Insira o valor de n:"))
i=len(str(n))
repete=False
while i>=2:
    if ( ((n%(10**i))//(10 **(i-1))) == ((n%(10**(i-1)))//(10**(i-2)))):
        repete = True
    i-=1
if repete:
    print("sim")
else:
    print("não")