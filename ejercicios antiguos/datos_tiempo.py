import datetime

def delta(fecha_inicial:str,fecha_final:str):
  fecha_inicial=datetime.datetime.strptime(fecha_inicial,'%Y-%m-%d %H:%M:%S')
  fecha_final=datetime.datetime.strptime(fecha_final,'%Y-%m-%d %H:%M:%S')
  tdelta=(fecha_final - fecha_inicial)
  a=str(tdelta).split()
  b=a[-1].split(':')
  return (f'{a[0]} dias, {b[0]} horas ')
  
c=int(input())
# datos=[]
m=[]
lis=[]
acomulador=0
for i in range(c):
  dato=input()
  
  if len(lis)>=1:
    m+=[delta(lis[-1],dato)]
  lis+=[dato]

for i in m:
  print(i)


  
