'''''
a1 = 1, a2 = 2 a3 = 1 + 2 = a1 + a2
an = a n – 1 + a n – 2 (n >= 3)
'''''

def fibonacci(numero):
    if numero == 1:
        return 1
    if numero == 2:
        return 2
    return fibonacci(numero - 1) + fibonacci(numero - 2)

numero = -1
enesimo = 0
while numero < 0:

    numero = int(input("Escribe un número para calcular el enésimo término de la serie de Fibonacci correspondiente: "))

    if numero >= 0:
        enesimo = fibonacci(numero)
    else:
        numero = int(input("Escribe un número mayor o igual que cero: "))

print("El " + str(numero) + "° numero de esta serie de Fibonacci es ", enesimo)
