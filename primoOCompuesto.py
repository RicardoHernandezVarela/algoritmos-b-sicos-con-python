numero = input("Escribe un número entero positivo > 1 para determinar si es primo o compuesto:")
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
          #print(lista[x])
      cuentaDivisible.append(divisible)
      cuenta += 1
      divisible = 0
    return cuentaDivisible

def esPrimo(numero):
    lista = generarLista(numero)
    cuentaDivisible = contarDivisibles(numero)
    #print(cuentaDivisible)
    #print(lista.index(numero))
    #print(cuentaDivisible[lista.index(numero)])
    if cuentaDivisible[lista.index(numero)] <= 2:
        print(str(numero) + " Es primo")
    else:
        print(str(numero) + " Es compuesto")


esPrimo(numero)
