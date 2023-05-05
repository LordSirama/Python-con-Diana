def A(m,n):
  if m==0:
    return n+1
  elif m>0 and n==0:
    return A(m-1,1)
  elif m>0 and n>0:
    return A(m-1,A(m, n-1))

e=[]
c=int(input("cantidad de casos: "))


for i in range(c):
  m=int(input('m: '))
  n=int(input('n: '))
  e+=[A(m,n)]

for i in e:
  print(i)

