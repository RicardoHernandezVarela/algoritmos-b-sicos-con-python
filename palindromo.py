mensaje1 = ""
while mensaje1 != "N":
  mensaje1 = input("Escribe una palabra para saber si es un palíndromo: ")
  mensaje2 = mensaje1[::-1]
  if mensaje1 == mensaje2:
    print("La palabra " + mensaje1 + " es un palíndromo")
    print(mensaje1 + " = " + mensaje2)
  else:
      print("La palabra " + mensaje1 + " no es un palíndromo")
      print(mensaje1 + " != " + mensaje2)
