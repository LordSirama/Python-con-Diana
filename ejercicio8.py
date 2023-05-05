with open('mensaje.txt','r') as archivo:  
  for i in archivo:
    print(i[::-1].lstrip('\n'))








