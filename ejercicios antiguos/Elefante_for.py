resistencia=int(input('Resistencia: '))
elefantes=int(input('Número elefantes: '))
suma=0
n=elefantes
llave=True
for i in range (1, elefantes+1):
  pesos=int(input("ingrese cuanto pesa el elefante: "))
  suma+=pesos
  if suma>resistencia and llave:
    n=i-1
    llave=False
print(n)
  