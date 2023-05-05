
def segundos(hora):
  
  if 'PM' in hora:
    hora=hora.rstrip('PM').split(':')
    horas=int(hora[0])+12
    segundos=int(hora[-1])
    minutos=int(hora[-2])
    if int(hora[0])==12:
      horas=12
    
    
  else:
    hora=hora.rstrip('AM').split(':')
    horas=int(hora[0])
    segundos=int(hora[-1])
    minutos=int(hora[-2])
    if horas==12:
      horas=0
    
  return round(100*(horas*3600 + minutos*60 +segundos)/86400,3)
  
b=int(input())
lis=[]
for i in range(b):
  c=input()
  lis+=[segundos(c)]

for i in lis:
  print(f'Loading day ... {i}%')

    