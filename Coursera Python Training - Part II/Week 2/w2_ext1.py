# Coursera Python Training 2
# Lucas Silva
# Week 2 - Exercício Extra 1 - Contando vogais e consoantes

def conta_letras(frase, contar="vogais"):
    cont_c=0
    cont_v=0
    for i in range(len(frase)):
        if frase[i] == ' ':
            pass
        elif frase[i]!='a' and frase[i]!='A' and frase[i]!='e' and frase[i]!='E' and frase[i]!='i' and frase[i]!='I' and frase[i]!='o' and frase[i]!='O' and frase[i]!='u' and frase[i]!='U':
            cont_c+=1
        else:
            cont_v+=1
                
    if contar == "consoantes":
        return cont_c
    else:
        return cont_v
