n=int(input('Partidos: '))

Ballenota=[]

R_b=0
R_m=0

for i in range (n):
  b=int(input(f'Resultado partido {i+1}: '))
  Ballenota+=[b]

for i in range (n):
  b=int(input(f'Resultado partido {i+1}: '))
  if Ballenota[i] > b:
    R_b+=2
  elif b> Ballenota[i]:
    R_m+=2
  else:
    R_m+=1
    R_b+=1

print(f'Ballenota Futbol Club: {R_b}')
print(f'Real Mandril: {R_m}')
