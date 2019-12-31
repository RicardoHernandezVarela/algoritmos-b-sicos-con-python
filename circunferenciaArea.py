import math
def circulo(radio):
  circunferencia = 2 * (math.pi*radio)
  area = math.pi * (radio**2)
  print("circunferencia = " + str(circunferencia))
  print("área = " + str(area))

circulo(10)