tablas = []
serie = []
inicio = 1
cuenta = 1

while len(tablas) < 15:
    serie.append(inicio)
    while len(serie) < 16:

        serie.append(cuenta * inicio)
        cuenta += 1

    tablas.append(serie)
    serie = []
    cuenta = 1
    inicio += 1

tablas.insert(0,["*", "**","**","**","**","**","**","**","**","**", "**", "**", "**", "**", "**","**"])
tablas.insert(0, ["*",1,2, 3, 4, 5 , 6 , 7, 8, 9, 10, 11, 12, 13, 14, 15])

for i in range(len(tablas)):
    for x in range(len(tablas[0])):
        primerValor = str(tablas[i][0]) + "*"
        tablas[i][0] = primerValor.rjust(5)
        print(repr(tablas[i][x]).rjust(5), end = ' ')
    print('\n')
