def capitalAcumulado(capital, tasa, semanas):
  duracionDias = semanas*7
  renta = (tasa * capital)/365
  capitalTotal = capital + renta*duracionDias
  print("Capital Total Acumulado = " + str(capitalTotal))

capitalAcumulado(1000, 0.06, 100)
