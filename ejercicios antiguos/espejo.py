def p_espejo(lista):
  s=0
  sumar=lambda l: sum(l) if l!=[] else 'hola'
  for i in range(1,len(lista)):
    if sumar(lista[:i])==sumar(lista[i:]):
      s+=1
  print(int(s))
lista=[]
for i in range(int(input())):
  lista+=[float(input())]
p_espejo(lista)
