import random

vida = 1
print("")
print("Bienvenido al Buscaminas!")
print("")

f1= [1, 2, 3]
f2= [4, 5, 6]
f3= [7, 8, 9]

print(f1)
print(f"{f2}    ¡Hay 3 bombas en estos 9 numeros!")
print(f3)

print("")

print("Regla: Tras elegir un numero, no podes volver a elegirlo")

print("")

minasF1 = random.sample(f1,1)[0]
minasF2 = random.sample(f2,1)[0]
minasF3 = random.sample(f3,1)[0]

eleccion1 = int(input("Eleji un numero y reza para que no contenga una mina!: "))

while eleccion1 != 0 and eleccion1 < 10 and vida == 1:
    if eleccion1 == minasF1 or eleccion1 == minasF2 or eleccion1 == minasF3:
        print("¡Perdiste!")
        vida = vida - 1
        break
    else:
        if eleccion1 != minasF1 or eleccion1 != minasF2 or eleccion1 != minasF3:
            print("Te salvaste")
            eleccion2 = int(input("Eleji otro numero y reza para que no contenga una mina!: "))
            if eleccion2 == eleccion1:
                print("Este numero ya fue descartado, perdiste por tramposo")
                vidas = 0
                break
            else:
                while eleccion2 != 0 and eleccion2 < 10 and vida == 1:
                    if eleccion2 == minasF1 or eleccion2 == minasF2 or eleccion2 == minasF3:
                        print("¡Perdiste!")
                        vida = vida - 1
                        break
                    else:
                        if eleccion2 != minasF1 or eleccion2 != minasF2 or eleccion2 != minasF3:
                            print("Te salvaste")
                            eleccion3 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                            if eleccion3 == eleccion2 or eleccion3 == eleccion1:
                                print("Este numero ya fue descartado, perdiste por tramposo")
                                vidas = 0
                                break
                            else:
                                while eleccion3 != 0 and eleccion3 < 10 and vida == 1:
                                    if eleccion3 == minasF1 or eleccion3 == minasF2 or eleccion3 == minasF3:
                                        print("¡Perdiste!")
                                        vida = vida - 1
                                        break
                                    else:
                                        if eleccion3 != minasF1 or eleccion3 != minasF2 or eleccion3 != minasF3:
                                            print("Te salvaste")
                                            eleccion4 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                            if eleccion4 == eleccion3 or eleccion4 == eleccion2 or eleccion4 == eleccion1:
                                                print("Este numero ya fue descartado, perdiste por tramposo")
                                                vidas = 0
                                                break
                                            else:
                                                while eleccion4 != 0 and eleccion4 < 10 and vida == 1:
                                                    if eleccion4 == minasF1 or eleccion4 == minasF2 or eleccion4 == minasF3:
                                                        print("¡Perdiste!")
                                                        vida = vida - 1
                                                        break
                                                    else:
                                                        if eleccion4 != minasF1 or eleccion4 != minasF2 or eleccion4 != minasF3:
                                                            print("Te salvaste")
                                                            eleccion5 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                                            if eleccion5 == eleccion4 or eleccion5 == eleccion3 or eleccion5 == eleccion2 or eleccion5 == eleccion1:
                                                                print("Este numero ya fue descartado, perdiste por tramposo")
                                                                vidas = 0
                                                                break
                                                            else:
                                                                while eleccion5 != 0 and eleccion5 < 10 and vida == 1:
                                                                    if eleccion5 == minasF1 or eleccion5 == minasF2 or eleccion5 == minasF3:
                                                                        print("¡Perdiste!")
                                                                        vida = vida - 1
                                                                        break
                                                                    else:
                                                                        if eleccion5 != minasF1 or eleccion5 != minasF2 or eleccion5 != minasF3:
                                                                            print("Te salvaste")
                                                                            eleccion6 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                                                            if eleccion6 == eleccion5 or eleccion6 == eleccion4 or eleccion6 == eleccion3 or eleccion6 == eleccion2 or eleccion6 == eleccion1:
                                                                                print("Este numero ya fue descartado, perdiste por tramposo")
                                                                                vidas = 0
                                                                                break
                                                                            else:
                                                                                while eleccion6 != 0 and eleccion6 < 10 and vida == 1:
                                                                                    if eleccion6 == minasF1 or eleccion6 == minasF2 or eleccion6 == minasF3:
                                                                                        print("¡Perdiste!")
                                                                                        vida = vida - 1
                                                                                        break
                                                                                    else:
                                                                                        if eleccion6 != minasF1 or eleccion6 != minasF2 or eleccion6 != minasF3:
                                                                                            vida = 2
                                                                                            while vida == 2:
                                                                                                print("¡GANASTE!")
                                                                                                break