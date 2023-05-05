lista=[]
for i in range(int(input())):
  lista+=[float(input())]

lista2=lista[:]
lista2.sort()
for i in lista2:
  print(lista.index(i)+1)

