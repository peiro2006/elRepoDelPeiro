#Importamos el valor Random para los juegos

import random

#Establecemos la variable para elejir los juegos

juegito = 0

#Mediante la estructura "while" (Mientras), comprobamos que mientra el valor de la variable "jueguito" no sea de 6, que se ejecute el super programa

while juegito != 6:
    
    #Mostramos en pantalla el menu de juegos

    print("")
    print("¡Binvenido al menu de juegos!")
    print("")
    print("1: BUSCAMINAS (Autor: Nazareno Peirone)")
    print("")
    print("2: AHORCADO (Autor: Augusto Baricco)")
    print("")
    print("3: ADIVINA EL NUMERO (Autora: Guadalupe Torres)")
    print("")
    print("4: PIEDRA, PAPEL O TIJERA (Autor: Matias Medina)")
    print("")
    print("5: BATALLA NAVAL (Autor: Ramiro Quintero)")
    print("")
    print("(Ingrese el numero 6 para salir del menu)")
    
    
    juegito = int(input("Ingrese el número del juego que desee jugar: "))

    if juegito == 1:

        #Establecemos las vidas

        vida = 1

        #Le damos la bienvenida al jugador mediante textos

        print("")
        print("Bienvenido al Buscaminas!")
        print("")

        #Establecemos las filas y las imprimimos en pantalla, imprimiendo tambien las reglas del juego

        f1= [1, 2, 3]
        f2= [4, 5, 6]
        f3= [7, 8, 9]

        print(f1)
        print(f"{f2}    ¡Hay 3 bombas en estos 9 numeros!")
        print(f3)
        print("")
        print("Regla 1: Tras elegir un numero, no podes volver a elegirlo")
        print("Regla 2: No se puede elegir un numero menor a 1, ni un numero mayor a 10")
        print("")

        #Asignamos una mina a un valor por cada fila de manera aleatoria

        minasF1 = random.sample(f1,1)[0]
        minasF2 = random.sample(f2,1)[0]
        minasF3 = random.sample(f3,1)[0]

        #Le pedimos al jugador que ingrese un numero

        eleccion1 = int(input("Eleji un numero y reza para que no contenga una mina!: "))

        #Ahora, arrancamos el algoritmo del juego:
        #Las aclaraciones iran al lado de los codigos

        if eleccion1 == 0 or eleccion1 > 9: #Aca se comprueba que el jugador no rompa la reglas del juego
                print("El numero ingresado rompe las reglas, perdiste")
                vida = vida - 1

        while eleccion1 != 0 and eleccion1 <= 9 and vida == 1: #Ingresamos los valores necesarios para iniciar el juego

            if eleccion1 == minasF1 or eleccion1 == minasF2 or eleccion1 == minasF3 : #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                print("¡Perdiste!")
                vida = vida - 1
                break
            else:
                if eleccion1 != minasF1 or eleccion1 != minasF2 or eleccion1 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                    print("Te salvaste")
                    eleccion2 = int(input("Eleji otro numero y reza para que no contenga una mina!: "))
                    if eleccion2 == eleccion1 or eleccion2 == 0 or eleccion2 > 9: #Aca se comprueba que el jugador no rompa la reglas del juego
                        print("El numero ingresado rompe las reglas, perdiste")
                        vida = vida - 1
                        break
                    else:
                        while eleccion2 != 0 and eleccion2 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                            if eleccion2 == minasF1 or eleccion2 == minasF2 or eleccion2 == minasF3 or eleccion2 == 0 or eleccion2 > 9: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                print("¡Perdiste!")
                                vida = vida - 1
                                break
                            else:
                                if eleccion2 != minasF1 or eleccion2 != minasF2 or eleccion2 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                                    print("Te salvaste")
                                    eleccion3 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                    if eleccion3 == eleccion2 or eleccion3 == eleccion1 or eleccion3 == 0 or eleccion3 > 9: #Aca se comprueba que el jugador no rompa la reglas del juego
                                        print("El numero ingresado rompe las reglas, perdiste")
                                        vida = vida - 1
                                        break
                                    else:
                                        while eleccion3 != 0 and eleccion3 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                                            if eleccion3 == minasF1 or eleccion3 == minasF2 or eleccion3 == minasF3 or eleccion3 == 0 or eleccion3 > 9: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                                print("¡Perdiste!")
                                                vida = vida - 1
                                                break
                                            else:
                                                if eleccion3 != minasF1 or eleccion3 != minasF2 or eleccion3 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                                                    print("Te salvaste")
                                                    eleccion4 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                                    if eleccion4 == eleccion3 or eleccion4 == eleccion2 or eleccion4 == eleccion1 or eleccion4 == 0 or eleccion4 > 9:
                                                        print("El numero ingresado rompe las reglas, perdiste") #Aca se comprueba que el jugador no rompa la reglas del juego
                                                        vida = vida - 1
                                                        break
                                                    else:
                                                        while eleccion4 != 0 and eleccion4 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                                                            if eleccion4 == minasF1 or eleccion4 == minasF2 or eleccion4 == minasF3: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                                                print("¡Perdiste!")
                                                                vida = vida - 1
                                                                break
                                                            else:
                                                                if eleccion4 != minasF1 or eleccion4 != minasF2 or eleccion4 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                                                                    print("Te salvaste")
                                                                    eleccion5 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                                                    if eleccion5 == eleccion4 or eleccion5 == eleccion3 or eleccion5 == eleccion2 or eleccion5 == eleccion1 or eleccion5 == 0 or eleccion5 > 9:
                                                                        print("El numero ingresado rompe las reglas, perdiste") #Aca se comprueba que el jugador no rompa la reglas del juego
                                                                        vida = vida - 1
                                                                        break
                                                                    else:
                                                                        while eleccion5 != 0 and eleccion5 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                                                                            if eleccion5 == minasF1 or eleccion5 == minasF2 or eleccion5 == minasF3: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                                                                print("¡Perdiste!")
                                                                                vida = vida - 1
                                                                                break
                                                                            else:
                                                                                if eleccion5 != minasF1 or eleccion5 != minasF2 or eleccion5 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                                                                                    print("Te salvaste")
                                                                                    eleccion6 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                                                                    if eleccion6 == eleccion5 or eleccion6 == eleccion4 or eleccion6 == eleccion3 or eleccion6 == eleccion2 or eleccion6 == eleccion1 or eleccion6 == 0 or eleccion6 > 9:
                                                                                        print("El numero ingresado rompe las reglas, perdiste") #Aca se comprueba que el jugador no rompa la reglas del juego
                                                                                        vida = vida - 1
                                                                                        break
                                                                                    else:
                                                                                        while eleccion6 != 0 and eleccion6 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                                                                                            if eleccion6 == minasF1 or eleccion6 == minasF2 or eleccion6 == minasF3: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                                                                                print("¡Perdiste!")
                                                                                                vida = vida - 1
                                                                                                break
                                                                                            else:
                                                                                                if eleccion6 != minasF1 or eleccion6 != minasF2 or eleccion6 != minasF3: #Si el jugador elijio un numero sin mina, este finaliza el juego
                                                                                                    vida = 2
                                                                                                    while vida == 2:
                                                                                                        print("¡GANASTE!") #:D
                                                                                                        break 


    if juegito == 2:
        #Juego El Ahorcado#

        Palabras = ["esternocleidomastoideo","auriculares","zapatillas","bicicleta","musica","gato","codigo"]
        #randomchoice es para que seleccione aleatoriamente cualquier palabra de la variable palabras
        palabraclave = random.choice(Palabras)
        #Aca hace que la palabra elegida se transforme en guiones, varia dependiendo el largo de la palabra
        cadena = "-" * len(palabraclave)
        intentos=0
        print("Bienvenidos al ahorcado")
        while True:
            print(cadena)
            letra = input(" Ingrese una letra: ")
            #bucle for, pasa por toda la palabra la letra ingresada, si es correcta, cambia los guiones solo por esa letra.
            if letra in palabraclave:
                for i in range(len(palabraclave)):
                    if palabraclave[i]==letra:
                        cadena=cadena[:i]+letra+cadena[i+1:]
                        #Esta funcion hace que cambie la letra que coincide, va hasta i (coincide) la modifica y las demas siguen igual.
            else:
                intentos+=1
                if intentos == 1:
                    print(" ")
                    print("Error 1/5 La letra no coincide, vuelve a intentarlo!")
                elif intentos == 2:
                    print(" ")
                    print ("Error 2/5, La letra no coincide, vuelve a intentarlo!")
                elif intentos == 3:
                    print(" ")
                    print ("Error 3/5, La letra no coincide, vuelve a intentarlo!")            
                elif intentos ==4:
                    print(" ")
                    print ("Error 4/5, La letra no coincide, es tu última oportunidad!") 
                elif intentos == 5:
                    print(" ")
                    print (f"Error 5/5, haz perdido!la palabra oculta era {palabraclave}")
                    break
            if cadena == palabraclave:
                    print (f"felicidades, has ganado. La palabra oculta era: {palabraclave}")
                    break

    if juegito == 3:
        from random import randint

        #establecemos las variables para el juego

        intentos= 0 
        estimado = 0
        numero_secreto= randint (1,100)
        nombre= input ("Dime tu nombre: ")

        #damos las indicaciones al jugador para jugar

        print (f"{nombre}, pense un número entre 1 y 100, tenes 8 intentos para adivinar")

        #algoritmo para jugar

        while intentos < 8:
            estimado= int(input("Cual es el numero?: "))
            intentos += 1
            if estimado not in range(1,101):
                print("Tu número no se encuentra en el rango que va desde 1 a 100")
            elif estimado < numero_secreto:
                print("Mi numero es mas alto")
            elif estimado > numero_secreto:
                print("Mi numero es mas bajo")
            else:
                print (f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
                break 

        #algoritmo para las equivocaciones

        if estimado != numero_secreto:
            print (f"Lo siento se han agotado los intentos. El número secreto era {numero_secreto}")

    if juegito == 4:

        print("")
        print("Piedra = 1")
        print("Papel = 2        ¡Gana el mejor de 3!")
        print("Tijera = 3")
        print("")

        jugando= 0 
        rM = 0
        rJ = 0

        juego = [1,2,3]

        while rM != 3 and rJ != 3:
            eleccionMaquina = random.sample(juego,1)[0]
            eleccion = int(input("Eleji entre las 3: "))

            if eleccion == eleccionMaquina:
                print("Empate")

            if eleccion == 1 and eleccionMaquina == 3:
                print("La maquina eligió tijera, ganaste!")
                rJ = rJ + 1
            else:
                if eleccion == 1 and eleccionMaquina == 2:
                    print("La maquina eligió papel, perdiste!")
                    rM = rM + 1


            if eleccion == 2 and eleccionMaquina == 1:
                print("La maquina eligió piedra, ganaste!")
                rJ = rJ + 1
            else:
                if eleccion == 2 and eleccionMaquina == 3:
                    print("La maquina eligió tijera, perdiste!")
                    rM = rM + 1


            if eleccion == 3 and eleccionMaquina == 2:
                print("La maquina eligió papel, ganaste!")
                rJ = rJ + 1
            else:
                if eleccion == 3 and eleccionMaquina == 1:
                    print("La maquina eligió piedra, perdiste!")
                    rM = rM + 1

        while jugando == 0:
            if rJ == 3:
                print("¡Ganaste!")
                break
            else:
                if rM == 3:
                    print("¡Perdiste!")
                    break

    if juegito == 5:
       
        # Función para validar que el valor sea de 1 a 3
        def obtenerCoordenadaValida(mensaje):
            while True:
                valor = int(input(mensaje))
                if 1 <= valor <= 3:
                    return valor
                else:
                    print("Valor fuera de rango. Por favor ingrese un número entre 1 y 3.")

        # Creamos los tableros para cada jugador 
        tablero1 = [[0 for columnas in range(3)] for filas in range(3)]
        for filas in range(0, len(tablero1)):
            for columnas in range(0, len(tablero1[filas])): 
                tablero1[filas-1][columnas-1] = 1

        print("Tablero Jugador 1:")
        for filas in tablero1:
            print(filas)
        print(" ")

        tablero2 = [[0 for columnas2 in range(3)] for filas2 in range(3)]
        for filas2 in range(0, len(tablero2)):
            for columnas2 in range(0, len(tablero2[filas2])): 
                tablero2[filas2-1][columnas2-1] = 2

        print("Tablero Jugador 2:")
        for filas2 in tablero2:
            print(filas2)

        # La idea es permitir que cada jugador cargue sus barcos en una posición del tablero, barcos únicamente 1x1
        for i in range(3): # Cada jugador contará con 3 barcos
            n1 = obtenerCoordenadaValida("Jugador 1, ingrese la fila donde colocar su barco: ")
            n2 = obtenerCoordenadaValida("Jugador 1, ingrese columna donde colocar su barco: ")
            tablero1[n1-1][n2-1] = 0

        print("Tablero Jugador 1 después de colocar barcos:")
        for filas in tablero1:
            print(filas)

        for i in range(3): # Cada jugador contará con 3 barcos
            n3 = obtenerCoordenadaValida("Jugador 2, ingrese la fila donde colocar su barco: ")
            n4 = obtenerCoordenadaValida("Jugador 2, ingrese columna donde colocar su barco: ")
            tablero2[n3-1][n4-1] = 0

        print("Tablero Jugador 2 después de colocar barcos:")
        for filas in tablero2:
            print(filas)

        # Comienza el juego
        barcos1 = 3
        barcos2 = 3
        turno_jugador = 1  # Empieza el jugador 1

        while barcos1 != 0 and barcos2 != 0:
            if turno_jugador == 1:
                print("Turno jugador número 1")
                n3 = obtenerCoordenadaValida("Ingrese fila: ")
                n4 = obtenerCoordenadaValida("Ingrese columna: ")
                
                if tablero2[n3-1][n4-1] == 0:
                    barcos2 -= 1
                    print("¡HUNDISTE UN BARCO!")
                    if barcos2 == 0:
                        break  # El juego termina si todos los barcos del jugador 2 están destruidos
                else:
                    print("FALLASTE")
                    turno_jugador = 2  # Cambia el turno al jugador 2

            elif turno_jugador == 2:
                print("Turno jugador número 2")
                n1 = obtenerCoordenadaValida("Ingrese fila: ")
                n2 = obtenerCoordenadaValida("Ingrese columna: ")
                
                if tablero1[n1-1][n2-1] == 0:
                    barcos1 -= 1
                    print("¡HUNDISTE UN BARCO!")
                    if barcos1 == 0:
                        break  # El juego termina si todos los barcos del jugador 1 están destruidos
                else:
                    print("FALLASTE")
                    turno_jugador = 1  # Cambia el turno al jugador 1

        # Resultados finales
        if barcos1 == 0:
            print("JUGADOR 2 ES EL GANADOR")   
        elif barcos2 == 0:
            print("JUGADOR 1 ES EL GANADOR")
            

