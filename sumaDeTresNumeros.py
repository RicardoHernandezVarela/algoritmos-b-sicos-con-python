def compararSuma(numero1, numero2, numero3):
  if numero1 == numero2+numero3:
    print("numero1 = numero2 + numero3")
    print(str(numero1) + " = " + str(numero2) + " + " + str(numero3))
  elif numero2 == numero1+numero3:
    print("numero2 = numero1 + numero3")
    print(str(numero2) + " = " + str(numero1) + " + " + str(numero3))
  elif numero3 == numero1+numero2:
    print("numero3 = numero1 + numero2")
    print(str(numero3) + " = " + str(numero1) + " + " + str(numero2))
  else:
    print("Ningún número es la suma de los otros dos")

compararSuma(750, 50, 800)