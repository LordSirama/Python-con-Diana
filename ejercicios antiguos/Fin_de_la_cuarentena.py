from datetime  import datetime  #Aquí se importa solo el paquete se usará

c=int(input('Casos: '))
datos=[]
for i in range(c):
  dato=input('Dato: ').split()
  fecha1=datetime.strptime(dato[-2],"%Y-%m-%d")

  fecha2=datetime.strptime(dato[-1],"%Y-%m-%d")

  dias=(fecha2-fecha1).days
  horas=dias*24
  segundos=horas*3600
  minutos=segundos//60
  datos+=[f'{dias} dias = {horas} horas = {minutos} minutos = {segundos} segundos']

for i in datos:
  print(i)
  
# 3
# Italia 2020-03-09 2020-05-18
# Japon 2020-04-07 2020-05-06
# Colombia 2020-03-25 2020-09-01

# 70 dias = 1680 horas = 100800 minutos = 6048000 segundos
# 29 dias = 696 horas = 41760 minutos = 2505600 segundos
# 160 dias = 3840 horas = 230400 minutos = 13824000 segundos
