tiempoMinutos = 1

while tiempoMinutos != 0:
    tiempo = input("Escribe el tiempo del corredor: ")

    tiempo = tiempo.split(",")

    tiempo[0] = int(tiempo[0])
    tiempo[1] = int(tiempo[1])

    distancia = 1500
    tiempoMinutos = tiempo[0]*60 + (tiempo[1])

    if tiempoMinutos > 0:
        velocidad = distancia/tiempoMinutos
        print("Tiempo: " + str(tiempo[0]) + " minutos " + str(tiempo[1]) + " segundos" + " Velocidad: " + str(velocidad) + " metros/segundos")
    else:
        print("Fin de entrada de datos")