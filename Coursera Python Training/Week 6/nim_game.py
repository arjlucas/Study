def jogar():
    x = int(input(("Bem vindo ao jogo do NIM ! Escollha 1 para jogar uma partida ou 2 para jogar um campeonato:")))
    while (x != 1 and x != 2):
        x = int(input("Por favor, escolha entre 1 ou 2:"))
    if x == 1:
        print("Você escolheu Partida")
        partida()
    else:
        print("Você escolheu Campeonato !")
        campeonato()
    print("Fim de Jogo !")


def computador_escolhe_jogada(n, m):
    if n <= m:
        x = n
    elif n - (m + 1) <= m:
        x = n - (m + 1)
    else:
        x = m
        for i in range(1, m + 1):
            if (n - i) % (m + 1) == 0:
                x = i
                break

    if x == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", x, "peças.")
    return x


def usuario_escolhe_jogada(n, m):
    x = int(input("Quantas peças quer retirar ?"))
    while (x < 1) or (x > m) or (x>n):
        x = int(input("Por favor insira uma jogada válida:"))
    if x == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou", x, "peças.")
    return x


def campeonato():
    placar_usuario = 0
    placar_computador = 0
    for i in range(1, 4):
        print("Rodada",i)
        if partida() == 1:
            placar_usuario += 1
        else:
            placar_computador += 1
    print("Fim de Campeonato !")
    print("Placar Final: Usuário", placar_usuario, "x", placar_computador, "Computador")


def partida():
    n = int(input("Quantas peças no tabuleiro ?"))
    m = int(input("Qual o limite de peças por jogada ?"))
    vencedor = 0

    if n % (m + 1) == 0:
        print("Você começa")
        while (n != 0):
            print("O número de peças no tabuleiro é:", n)
            n -= usuario_escolhe_jogada(n, m)
            if (n == 0):
                print("Você Venceu !")
                vencedor = 1
                break
            else:
                n -= computador_escolhe_jogada(n, m)
                if n == 0:
                    print("O Computador Venceu !")
                    vencedor = 2
                    break
    else:
        print("Computador começa")
        while (n != 0):
            print("O número de peças no tabuleiro é:", n)
            n -= computador_escolhe_jogada(n, m)
            if (n == 0):
                print("O Computador Venceu !")
                vencedor = 2
                break
            else:
                n -= usuario_escolhe_jogada(n, m)
                if n == 0:
                    print("Você Venceu !")
                    vencedor = 1
                    break
    return vencedor

jogar()