"""
import math

sumatoria = 1 + potencia
for i in range(2, numero + 1):
    sumatoria = sumatoria + (potencia**i/math.factorial(i))

print("a :", sumatoria)
"""

#n! = n × (n-1)!

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)


numero = int(input("Escribe la cantidad de terminos a evaluar: "))
potencia = int(input("Escribe la potencia para e: "))

sumatoria = 1 + potencia
error = 0.0001
aproximacion = 0.1

while aproximacion > error:

    aproximacion = potencia**numero/factorial(numero)

    if aproximacion < error:
        for i in range(2, numero + 1):
            sumatoria += (potencia ** i / factorial(i))
    else:
        numero = int(input("Escribe una cantidad de terminos mayor: "))

print("e^" + str(potencia) + " =",sumatoria)