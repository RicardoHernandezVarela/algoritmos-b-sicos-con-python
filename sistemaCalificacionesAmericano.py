
seguir = "s"

while seguir == "s":
    calificacion = float(input("Escribe tú calificación: "))

    if calificacion >= 90:
        print(str(calificacion) + " equivale a A en el sistema americano")

    elif 90 > calificacion >= 80:
        print(str(calificacion) + " equivale a B en el sistema americano")

    elif 80 > calificacion >= 70:
        print(str(calificacion) + " equivale a C en el sistema americano")

    elif 70 > calificacion >= 69:
        print(str(calificacion) + " equivale a D en el sistema americano")

    elif calificacion < 69 :
        print(str(calificacion) + " equivale a F en el sistema americano")

    seguir = input("¿Quieres seguir? s = si, n = no")