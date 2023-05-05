n = int(input('Datos: '))
datos = []

for i in range(n):
    d = input('valor: ').upper()
    if 'POSITIVA' in d:
        d = d.split()
        d[1], d[-1] = int(d[1]), int(d[-1])
        datos.append(d)

datos = sorted(datos, reverse=True, key=lambda parametro: parametro[1])
datos = sorted(datos, reverse=True, key=lambda parametro: parametro[-1])

for i in datos:
    i[1], i[-1] = str(i[1]), str(i[-1])
    print(' '.join(i[1:]))
