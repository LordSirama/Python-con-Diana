def A(numero:str):
  return numero[:3]
  
def B(numero:str):
  numero=A(numero)
  if int(numero) in range(300,401):
    return f'Número: {numero}, Tipo de contacto: Celular'
  if int(numero)>600:
    return f'Número: {numero}, Tipo de contacto: fijo'

def C(numero:str):
  return numero[-7:]

def D(numero:str):
  n=A(numero)
  pares=''
  impares=''
  for i in numero:
    if int(i)%2==0:
      pares+=i
    else:
      impares+=i
  if int(n) in range(300,401):
    print(f'Numero:{numero} y sus números impares son {impares}')
  else:
    print(f'Numero:{numero} y sus números pares son {pares}')
    
D('7654321')
             
  

