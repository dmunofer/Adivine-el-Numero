from random import randint

SI = ("s", "si", "y", "yes", "1")

def pedir_entrada_si_o_no(invitacion):
    """Por defecto, cualquier respuesta no contemplada vale NO"""
    try:
        return input(invitacion).lower() in SI
    except:
        return False

ayuda = pedir_entrada_si_o_no("¿Desea jugar conociendo los límites?")

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
    if ayuda:
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

def jugar_una_vez(numero, minimo, maximo):
    intento = pedir_numero_limite("Adivine el número", minimo, maximo)
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        victoria = False
    else:
        print("¡Ha ganado!")
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo

def jugar_una_partida(numero, minimo, maximo):
    victoria = False
    while not victoria:
        victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)

def decidir_limites():
    while True:
        nivel = pedir_numero("Elige un nivel de dificultad del 1 al 4: ")
        if nivel<1 or nivel>4:
            print("Error. Introduce un nivel válido")
        elif nivel==1:
            minimo=0
            maximo=100
        elif nivel==2:
            minimo = 0
            maximo= 1000
        elif nivel==3:
            minimo =0
            maximo=1000000
        elif nivel==4:
            minimo=0
            maximo=1000000000000
        return minimo, maximo

def jugar():
    minimo, maximo = decidir_limites()
    while True:
        numero = randint(minimo,maximo)
        jugar_una_partida(numero, minimo, maximo)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return
