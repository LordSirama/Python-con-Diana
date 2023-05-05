n=int(input("cantidad de miembros: "))
m=int(input("numero de partidas de bingo: "))

miembros=range(1,n+1)
partidas_ganadas=n*[0]



for i in range(m):
  a=int(input('Miembro ganador: '))
  posicion=miembros.index(a)
  partidas_ganadas[posicion]+=1

maximo=max(partidas_ganadas)

if partidas_ganadas.count(maximo)==1:
  
  posicion=partidas_ganadas.index(maximo)
  
  print(miembros[posicion])

else:
  c=0
  cm=0
  for i in partidas_ganadas:

    if i==maximo:
      
      print(miembros[c])

      cm+=1
      if cm==partidas_ganadas.count(maximo):
        break
    c+=1
    

