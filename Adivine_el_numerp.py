from random import randint
num = randint(0,99)
intentos = 0
guess = int(input('Adivina el número del 0 al 99: '))
while guess!=num:
    if guess<num:
        print('El número es mayor')
    else:
        print('El número es menor')
    intentos +=1
    guess = int(input('Prueba con otro número: '))

if guess == num:
    print('Enhorabuena, adivinaste el número en '+ f'{intentos} intentos, '+ 'el número era el '+ f'{num}')








