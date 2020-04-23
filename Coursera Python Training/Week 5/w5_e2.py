def maior_primo(n):
    aux = n
    i = 1
    primo = False
    cdiv = 0
    cdivpr = 0
    while primo == False:
        aux = n - 1
        while i <= aux:
            if aux % i == 0:
                cdiv += 1
            if i == 1 or i == aux:
                cdivpr += 1
            i += 1
        if cdiv == cdivpr:
            primo = True
    return aux