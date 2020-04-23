def maior_primo(n):
    maior = 1
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
                maior = i
    return maior