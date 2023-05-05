e=[]
n=input('Número: ')

def parImpar(n):
  
  if n%2!=0:
    
    return True
  
  return False

def hyperpar(n):
  """
  Imprime Hyperpar si el número está compuesto por solo números pares, e imprime No es hyperpar si hay al menos un número impar
  """
  Hyper='Hyperpar'

  for i in n:
  
    if parImpar(int(i)):
      Hyper='No es hyperpar'
      break

  print(Hyper)

while int(n)!=-1:
  #Este ciclo while se ejecuta hasta que se ingrese un -1
  #Va almacenando los string de los números mayores a -1
  e+=[n]
  n=input('Número')

for i in e:
   hyperpar(i)




