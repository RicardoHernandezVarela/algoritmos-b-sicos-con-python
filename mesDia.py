seguir = "s"
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

mes = int(input("Introduzca un mes 1 para enero, 2 para febrero, 3 para Marzo, 4 para abril, 5 para mayo, 6 para junio, "
          "\n 7 para julio, 8 para agosto, 9 para septiembre, 10 para octubre, 11 para noviembre y 12 para diciembre "))

dia = int(input("Escribe un día entre 1 y 31 "))

while mes <= 0 or mes > 12 or dia <= 0 or dia > 31:

    if mes <= 0 or mes > 12:
        mes = int(input(str(mes) + " no es una opción valida para el mes, introduce un número entre 1 y 12 "))

    if dia <= 0 or dia > 31:
        dia = int(input(str(dia) + " no es una opción valida para el día, introduce un número entre 1 y 31 "))

print(str(dia) + " de " + str(meses[mes-1]))

