def ruleta():
    from random import randint
    n=int(input('Ingresa el número de jugadores (no más de 6): '))
    jugadores=[]

    for j in range(n):
      jugadores+=[input(f'Nombre del jugador {j+1}: ').title()]
    
    disparo=randint(0,5)
    for i in range(6):
        input(f'Presiona enter para disparar {chr(0x1f52b)} ')
        if i == disparo:
            print(f'¡Ha muerto {jugadores[i%n]}! \u2620')
            break
ruleta()