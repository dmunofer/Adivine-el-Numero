from random import randint
mejores_puntuaciones = []
nivel = int(input('Escoge un nivel de dificultad del 1 al 5 (si quieres que juegue la IA introduce 5 ): '))
if nivel == 1:
    min = 0
    max = 100
    ayuda = int(input('Si quieres saber el máximo y mínimo del nivel introduce 1, si no, introduce 0: '))
    if ayuda == 1:
        print('El número está entre ' + f'{min} y ' + f'{max}')
    num = randint(0,100)
    intentos = 1
    max_intentos = 10
    guess = int(input('Adivina el número: '))
    if intentos == max_intentos:
        print('Lo siento, te has quedado sin intentos, el número era el '+f'{num}')
    while guess!=num:
        if guess<=max and guess>=min:
            if guess<num:
                print('El número es mayor')
            elif guess>num:
                print('El número es menor')
        else:
            print('Error. El número introducido está fuera del rango del nivel escogido')
        intentos +=1
        guess = int(input('Prueba con otro número: '))
    if guess == num:
        nombre = input('Introduce tu nombre para registrar tu puntuación: ')
        mejores_puntuaciones.append((nombre, intentos))
        print('Enhorabuena '+ f'{nombre}, adivinaste el número en '+ f'{intentos} intentos, '+ 'el número era el '+ f'{num}')

elif nivel == 2:
    min = 0
    max = 1000
    ayuda = int(input('Si quieres saber el máximo y mínimo del nivel introduce 1, si no, introduce 0: '))
    if ayuda == 1:
        print('El número está entre ' + f'{min} y ' + f'{max}')
    num = randint(0,1000)
    intentos = 1
    max_intentos=100
    guess = int(input('Adivina el número: '))
    if intentos == max_intentos:
        print('Lo siento, te has quedado sin intentos, el número era el '+f'{num}')
    while guess!=num:
        if guess<=max and guess>=min:
            if guess<num:
                print('El número es mayor')
            elif guess>num:
                print('El número es menor')
        else:
            print('Error. El número introducido está fuera del rango del nivel escogido')
        intentos +=1
        guess = int(input('Prueba con otro número: '))
    if guess == num:
        nombre = input('Introduce tu nombre para registrar tu puntuación: ')
        mejores_puntuaciones.append((nombre, intentos))
        print('Enhorabuena '+ f'{nombre}, adivinaste el número en '+ f'{intentos} intentos, '+ 'el número era el '+ f'{num}')

elif nivel == 3:
    min = 0
    max = 1000000
    ayuda = int(input('Si quieres saber el máximo y mínimo del nivel introduce 1, si no, introduce 0: '))
    if ayuda == 1:
        print('El número está entre ' + f'{min} y ' + f'{max}')
    num = randint(0,1000000)
    intentos = 1
    max_intentos=1000
    guess = int(input('Adivina el número: '))
    if intentos == max_intentos:
        print('Lo siento, te has quedado sin intentos, el número era el '+f'{num}')
    while guess!=num:
        if guess<=max and guess>=min:
            if guess<num:
                print('El número es mayor')
            elif guess>num:
                print('El número es menor')
        else:
            print('Error. El número introducido está fuera del rango del nivel escogido')
        intentos +=1
        guess = int(input('Prueba con otro número: '))
    if guess == num:
        nombre = input('Introduce tu nombre para registrar tu puntuación: ')
        mejores_puntuaciones.append((nombre, intentos))
        print('Enhorabuena '+ f'{nombre}, adivinaste el número en '+ f'{intentos} intentos, '+ 'el número era el '+ f'{num}')
elif nivel == 4:
    min = 0
    max = 1000000000000
    ayuda = int(input('Si quieres saber el máximo y mínimo del nivel introduce 1, si no, introduce 0: '))
    if ayuda == 1:
        print('El número está entre ' + f'{min} y ' + f'{max}')
    num = randint(0,1000000000000)
    intentos = 1
    max_intentos = 100000
    guess = int(input('Adivina el número: '))
    if intentos == max_intentos:
        print('Lo siento, te has quedado sin intentos, el número era el '+f'{num}')
    while guess!=num:
        if guess<=max and guess>=min:
            if guess<num:
                print('El número es mayor')
            elif guess>num:
                print('El número es menor')
        else:
            print('Error. El número introducido está fuera del rango del nivel escogido')
        intentos +=1
        guess = int(input('Prueba con otro número: '))
    if guess == num:
        nombre = input('Introduce tu nombre para registrar tu puntuación: ')
        mejores_puntuaciones.append((nombre, intentos))
        print('Enhorabuena '+ f'{nombre}, adivinaste el número en '+ f'{intentos} intentos, '+ 'el número era el '+ f'{num}')
elif nivel == 5:     # He probado este nivel con números más pequeños y funciona. La IA consigue adivinar el número, pero mi ordenador no es capaz de completar el nivel del 1000000000000
    min = int(input('Introduce el mínimo de los números que adivinará la IA (mayor o igual que 0) : '))
    max = int(input('Introduce el mínimo de los números que adivinará la IA (mayor que el mínimo) : '))
    num = randint(min,max)
    intentos = 1
    max_intentos = 100000
    guess = randint(min,max)
    if intentos == max_intentos:
        print('Lo siento, te has quedado sin intentos, el número era el '+f'{num}')
    while guess!=num:
        if guess<num:
            min = guess
            guess = randint(min,max)
        elif guess>num:
            max = guess
            guess = randint(min,max)
            intentos +=1
    if guess == num:
        nombre = 'IA'
        mejores_puntuaciones.append((nombre, intentos))
        print('Enhorabuena '+ f'{nombre}, adivinaste el número en '+ f'{intentos} intentos, '+ 'el número era el '+ f'{num}')
else:
    print('Error. El nivel debe ser 1, 2, 3, 4 o 5')