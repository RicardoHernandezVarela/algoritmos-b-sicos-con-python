numero = input("Escribe un número para determinar los números primos iguales o menores que él:")
numero = int(numero)

def generarLista(numero):
  lista = []
  for x in range(numero):
      lista.append(numero-x)
  #print(lista)
  return lista

def contarDivisibles(numero):
    lista = generarLista(numero)
    print(lista)
    cuentaDivisible = []
    divisible = 0
    cuenta = 0
    while cuenta < numero:
      for x in range(len(lista)):
        if lista[cuenta]%(lista[x]) == 0:
          divisible += 1
      cuentaDivisible.append(divisible)
      cuenta += 1
      divisible = 0
    return cuentaDivisible

def esPrimo(numero):
    lista = generarLista(numero)
    cuentaDivisible = contarDivisibles(numero)
    for x in range(len(cuentaDivisible)):
        if cuentaDivisible[x] <= 2:
            print(str(lista[x]) + " Es primo")

esPrimo(numero)
