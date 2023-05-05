#Creamos un programa que calcule la suma de dos números 

a=int(input('Ingrese el primer número: '))
b=int(input('Ingrese el segundo número: '))


if a%b ==0:
  print(f'{a} es divisible por {b}')
else:
  print(f'{a} no es divisible por {b}')