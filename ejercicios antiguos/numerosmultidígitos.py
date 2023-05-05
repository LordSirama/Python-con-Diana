c=set('12345')
multi=[]
n=input()
while n!='0':
  if c<=set(n):
    multi+=['Multidigito']
  else:
    multi+=['No es multidigito']
  n=input()

for i in multi:
  print(i)