numero1 = float(input("Escribe un número real "))
numero2 = float(input("Escribe otro número real "))

operacionDeseada = input("¿Qué operación deseas realizar con estos números, 1 = suma, 2 = multiplicación, 3 = división ")

if operacionDeseada == "1":
    suma = numero1 + numero2
    print(suma)
elif operacionDeseada == "2":
    multiplicacion = numero1 * numero2
    print(multiplicacion)
elif operacionDeseada == "3":
    division = numero1 / numero2
    print(division)
