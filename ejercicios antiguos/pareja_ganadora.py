a=[]

for i in range(2000):
  b=int(input())
  a+=[b]
  if b==0:
    break
    
a.pop()

c=len(a)
suma=0


for i in range (c):
  
  diana=a[i]
  pasajerox=1995-diana

  if pasajerox in a:
    suma+=1
    
print(suma//2)



