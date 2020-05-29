# Coursera Python Training 2
# Lucas Silva
# Week 2 - Exercício Extra 2 - Ordem Lexicográfica

def primeiro_lex(lista):
    lex=[]
    for i in range(len(lista)):
        lex.append(ord(lista[i][0]))
    #lex.sort()
    #print(lex)
    x=lex.index(min(lex))
    return lista[x]