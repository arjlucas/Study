# Coursera Python Training 1
# Lucas Silva
# Week 9 - Exercício Único - Similaridades entre Textos

# A partir da assinatura conhecida de um portador de COH-PIAH, seu programa 
# deverá receber diversos textos e calcular os valores dos diferentes traços 
# linguísticos desses textos para compará-los com a assinatura dada.

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similaridade=0
    for i in range(len(as_a)):
        similaridade+= abs(as_a[i]-as_b[i])
    similaridade = similaridade / len(as_a)
    return similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    # Separando sentenças para cada texto carregado e armazenado no
    # vetor de textos
    for i in range(len(textos)):
        # Contador do tamanho das palavras do texto
        cont_char=0

        # Contador do número de palavras
        cont_pal=0

        # Contador do número de palavras diferentes
        pal_dif=0
    
        # Tamanho médio das Sentenças
        tam_med_sen = 0
    
        # Complexidade Média das Sentenças
        complex_sen = 0
    
        # sentencas constitui uma lista contendo cada sentenca separada do 
        # texto na posição i da lista textos
        sentencas=separa_sentencas(textos[i])
    
        # Contador de Sentenças
        cont_sen = len(sentencas)
    
        # Contador de Frases
        cont_fra = 0
    
        # Tamanho Médio de Frases
        tam_med_fra = 0
        
        # Lista vazia de teste para calcula da R-Hapax Legomana
        teste=[]
    
        for j in range(len(sentencas)):
            # Frases constitui uma lista contendo cada frase separada da sentenca
            # na posição j da lista sentencas
            frases=separa_frases(sentencas[j])
            cont_fra = len(frases)
        
            for k in range(len(frases)):
                # Palavras constitui uma lista contendo cada palavra separada da
                # frase na posição k do lista frases
                palavras=separa_palavras(frases[k])
                # pal_uni = n_palavras_unicas(palavras)
                pal_dif += n_palavras_diferentes(palavras)
                # Conta o numero de palavras no vetor palavras
                cont_pal += len(palavras)
            
                for l in range(len(palavras)):
                    # Conta a quantidade de caracteres em cada palavra de cada posição do vetor palavras
                    cont_char += len(palavras[l])
                    teste.append(palavras[l])
        
        pal_un_tex = n_palavras_unicas(teste)
        rel_hpx_lego = pal_un_tex / cont_pal
        tam_med_pal = cont_char / cont_pal
        rel_type_token = pal_dif / cont_pal
        tam_med_sen = cont_char / cont_pal
        complex_sen = cont_fra / cont_sen
        tam_med_fra = cont_char / cont_fra
    
    # Falta calcular a Razão Hapax Legomana após a Type Token
    return [tam_med_pal, rel_type_token, rel_hpx_lego, tam_med_sen, complex_sen, tam_med_fra]
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass


# Código recebe a assinatura do Perfil referencial
assinatura_ref = le_assinatura()

# Os textos a serem analisados são carregados via função
textos = le_textos()



    
    # A Ordem da Assinatura é = [wal, ttr, hlr, sal, sac, pal]
    # assinatura = [tam_med_pal, rel_ty_token, raz_hapax_legomana, tam_med_sen, comp_sen, tam_med_fra]
    

