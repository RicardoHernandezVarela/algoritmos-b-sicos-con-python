def sumaSerie(semilla, limite):
  serie = [semilla]
  cuenta = 1
  suma = semilla

  while serie[-1] != limite:
    siguiente = serie[cuenta-1] + 3
    serie.append(siguiente)
    suma += siguiente
    cuenta += 1

  print(serie)
  print(suma)

sumaSerie(3, 99)