n = int(input('Cantidad de números: '))
lista = []
registro = []

for i in range(n):
    a = int(input('Valor: '))
    lista += [a]


def cont(lista):
    registro = []
    veces = []
    for i in lista:
        if not i in registro:
            registro += [i]
            veces += [f'{i}:{lista.count(i)}']
    return veces
