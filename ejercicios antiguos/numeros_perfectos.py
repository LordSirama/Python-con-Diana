def perfecto(n):
  div=0
  for i in range(1,n):
    if n%i==0:
      div+=i

  if div==n:
    
    return f'{n} es perfecto'
    
  return f'{n} no es perfecto'
    

perfectos=[]

n=int(input("valores a evaluar: "))

for i in range(n):
  b=int(input("valores: "))

  perfectos+=[perfecto(b)]

for i in perfectos:
  print(i)