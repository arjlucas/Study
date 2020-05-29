# Coursera Python Training 2
# Lucas Silva
# Week 2 - Exercício 2 - Menor nome

def menor_nome(nomes):
    tam=[]
    for i in range(len(nomes)):
        x = nomes[i]
        x=x.strip()
        x=x.capitalize()
        nomes[i]=x
        tam.append(len(nomes[i]))
    
    for i in range(len(tam)):
        if tam[i] == min(tam):
            menor=tam.index(tam[i])
            break
    
    return nomes[menor]

    
