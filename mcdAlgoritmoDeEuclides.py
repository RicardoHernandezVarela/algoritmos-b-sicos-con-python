def mcd(may, men):
    divisores = []
    modulo = may % men
    divisores.append(modulo)
    cuenta = 1
    if modulo == 0:
        print(men)
    else:
        modulo = men % divisores[cuenta - 1]
        divisores.append(modulo)

        while modulo != 0:
            modulo = divisores[cuenta - 1] % divisores[cuenta]
            divisores.append(modulo)
            cuenta += 1
        print(divisores)
        print(divisores[cuenta - 1])


mcd(45,25)
