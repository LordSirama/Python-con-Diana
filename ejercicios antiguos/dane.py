a=int(input('Número de días: '))
c=0
l=[]

for i in range (1,a+1):
  b=float(input('Promedio de nacimientos: '))
  T=b*i
  nh=T-c
  c+=nh

  l+=[nh]

for i in l:
  print(round(i))
  
  