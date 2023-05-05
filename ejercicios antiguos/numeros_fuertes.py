#factorial=lambda n: 1 if n<=1 else n*factorial(n-1)

from math import factorial

def fuerte(n):
  s=0
  for i in str(n):
     s+=factorial(int(i))
  if s==n:
    return f"{n} es fuerte"
  return  f"{n} no es fuerte"
e=[]
c=int(input())
for i in range(c):
  n=int(input())
  e+=[fuerte(n)]
  
for i in e:
  print(i)
  

