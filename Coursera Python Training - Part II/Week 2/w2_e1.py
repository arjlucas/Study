# Coursera Python Training 2
# Lucas Silva
# Week 2 - Exercício 1 - Letras Maiúsculas

def maiusculas(frase):
    maiusculas=""
    for i in range(len(frase)):
        if ord(frase[i])>64 and ord(frase[i])<91:
            maiusculas+=frase[i]
    return maiusculas