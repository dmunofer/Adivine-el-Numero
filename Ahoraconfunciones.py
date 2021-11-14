from random import randint

registro = []
SI = ("s", "si", "y", "yes", "1")

def pedir_entrada_si_o_no(invitacion):
    """Por defecto, cualquier respuesta no contemplada vale NO"""
    try:
        return input(invitacion).lower() in SI
    except:
        return False

def pedir_numero(invitacion):
    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            print("Solo están autorizados los caracteres [0-9]")
        else:
            return entrada

def pedir_numero_limite(invitacion, minimo, maximo):
    if pedir_entrada_si_o_no("¿Desea jugar conociendo los límites?"):
        while True:
            invitacion = "{} entre {} y {} incluidos".format(invitacion, minimo, maximo)
            entrada = pedir_numero(invitacion)
            if minimo <= entrada <= maximo:
                return entrada
    else:
        while True:
            invitacion = "{}".format(invitacion)
            entrada = pedir_numero(invitacion)
            if minimo <= entrada <= maximo:
                return entrada

def jugar_una_vez(numero, minimo, maximo, intentos, max_intentos):
    intento = pedir_numero_limite("Adivine el número", minimo, maximo)
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        intentos+=1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        intentos+=1
        victoria = False
    else:
        print('¡Ha ganado!')
        nombre = input("Introduzca su nombre para registrar su puntuación: ")
        registro.append((nombre,intentos))
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo, intentos, max_intentos

def jugar_una_partida(numero, minimo, maximo, intentos, max_intentos):
    victoria = False
    while not victoria:
        if intentos==max_intentos:
            print('Lo siento, te has quedado sin intentos')
            break
        else:
            victoria, minimo, maximo, intentos, max_intentos = jugar_una_vez(numero, minimo, maximo, intentos, max_intentos)

def decidir_limites():
    while True:
        nivel = pedir_numero("Elige un nivel de dificultad del 1 al 4: ")
        intentos = 0
        if nivel<1 or nivel>4:
            print("Error. Introduce un nivel válido")
        elif nivel==1:
            max_intentos = 10
            minimo=0
            maximo=100
        elif nivel==2:
            max_intentos = 100
            minimo=0
            maximo=1000
        elif nivel==3:
            max_intentos = 1000
            minimo=0
            maximo=1000000
        elif nivel==4:
            max_intentos = 1000000
            minimo=0
            maximo=1000000000000
        return minimo, maximo, intentos, max_intentos

def jugar():
    minimo, maximo, intentos, max_intentos = decidir_limites()
    while True:
        numero = randint(minimo,maximo)
        jugar_una_partida(numero, minimo, maximo, intentos, max_intentos)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return


def jugar_una_vez_IA(numero, minimo, maximo, intentos, max_intentos):
    intento = randint(minimo,maximo)
    if intento < numero:
        print( f'{intento}'+ ' es demasiado pequeño')
        minimo = intento + 1
        intentos+=1
        victoria = False
    elif intento > numero:
        print( f'{intento}'+ ' es demasiado grande')
        maximo = intento - 1
        intentos+=1
        victoria = False
    else:
        print('¡Ha ganado! el número era el '+ f'{numero}')
        nombre = 'IA'
        registro.append((nombre,intentos))
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo, intentos, max_intentos

def jugar_una_partida_IA(numero, minimo, maximo, intentos, max_intentos):
    victoria = False
    while not victoria:
        if intentos==max_intentos:
            print('Lo siento IA, te has quedado sin intentos')
            break
        else:
            victoria, minimo, maximo, intentos, max_intentos = jugar_una_vez_IA(numero, minimo, maximo, intentos, max_intentos)

def jugar_IA():
    minimo, maximo, intentos, max_intentos = decidir_limites()
    while True:
        numero = randint(minimo,maximo)
        jugar_una_partida_IA(numero, minimo, maximo, intentos, max_intentos)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return

def quien_juega():
    quien = input("¿Vas a jugar tú o la IA?")
    if quien != 'IA':
        return jugar()
    else:
        return jugar_IA()

