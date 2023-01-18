from random import randint
import time 

title = "Pokemon combate"
print("\n" + title + "\n" + "-" * len(title) + "\n")

pikachu_vida = 100
gengar_vida = 100

def pikachu_attack(atakp):
    if atakp == 1:
        print("Pikachu ataco con Trueno")
        return 10
    elif atakp == 2:
        print("Pikachu ataco con Rayo masivo")
        return 20

def gengar_attack(atakg):
    if atakg == 1:
        print("Gengar ataco con Polvo venenoso")
        return 15
    elif atakg == 2:
        print("Gengar ataco con Alucinacion")
        return 25

while pikachu_vida > 0 and gengar_vida > 0 :
    print("\nJugara primero Pikachu\n")
    atakp = randint(1, 2)
    pikachu_damage = pikachu_attack(atakp)
    gengar_vida -= pikachu_damage
    print("\nLa vida de Gengar es de: {}\n".format(gengar_vida))
    
    print("\nJugara Gengar\n")
    opcion = input("""\nTe toca a ti
    [1] Polvo venenoso
    [2] Alucinacion
    \nElije un ataque: """)
    if opcion == "1":
        gengar_damage = gengar_attack(1)
    elif opcion == "2":
        gengar_damage = gengar_attack(2)
    pikachu_vida -= gengar_damage
    print("\nLa vida de Pikachu es de: {}\n".format(pikachu_vida))
    time.sleep(1) 

if pikachu_vida > 0:
    print("\n" + "Pikachu ha ganado!" + "\n" + "-" * len("Pikachu ha ganado!") + "\n")
else:
    print("\n" + "Gengar ha ganado!" + "\n" + "-" *  len("Gengar ha ganado") + "\n")

input("\nEnter para salir\n")