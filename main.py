import random

carasDelDado = (1, 2, 3, 4, 5, 6)
def tirarDado():
    return random.choice(carasDelDado)

def tirada():
    print("Vamos a tirar el dado!")
    d = input("Presione 1 para tirar o 2 para salir: ")
    print("")
    while True:
        if d == ("1"):
            print("Cuantos dados desea tirar?")
            l = [None] * int(input())
            for i in l:
                print(tirarDado())
            tirada()
        elif d == ("2"):
            print("Hasta la proxima!")
            print("")
            break
        else:
            print("Seleccione una opcion valida")
            print("")
            tirada()


if __name__ == "__main__":
    tirada()