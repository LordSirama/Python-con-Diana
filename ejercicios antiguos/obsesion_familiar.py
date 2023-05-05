
def f(x):
  if x%123 == 0:
    return 0
  return 1+f(x+23)

e=[]
c=int(input())

for i in range(c):
  n=int(input())
  e+=[f(n)]
  
for i in e:
  print(i)