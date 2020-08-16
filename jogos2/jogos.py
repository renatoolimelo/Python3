import adivinhacao
import adivinhacao_v2
import forca

print("Bem vindo - por favor escolha seu jogo")
print()

escolha = 0
repetir = 1
escolher = 1

while ( repetir == 1 or escolher == 1):

    if (escolher == 1 and repetir == 2):
        escolha = 0

    while (escolha < 1 or escolha > 3):
        print("Advinhação    - 1")
        print("Advinhação_v2 - 2")
        print("Forca         - 3")
        print()
        escolha = int(input("Jogo escolhido:"))
        print()
        if (escolha < 1 or escolha > 3):
            print("Escolher um número entre 1 e 3")
            print()

    if ( escolha == 1 ):
        adivinhacao.jogar()
    elif ( escolha == 2 ):
        adivinhacao_v2.jogar()
    else:
        forca.jogar()

    repetir = 0
    while (repetir < 1 or repetir > 2):
        print()
        print("Quer jogar novamente?")
        print(" 1 - Sim / 2 - Não")
        print()
        repetir = int(input("Escolha: "))
        print()
        if (repetir < 1 or repetir > 2):
            print("Escolher número 1 ou 2")

    if( repetir == 1 ):
        continue

    escolher = 0
    while (escolher < 1 or escolher > 2):
        print()
        print("Quer escolher um novo jogo?")
        print(" 1 - Sim / 2 - Não")
        print()
        escolher = int(input("Escolha: "))
        if (escolher < 1 or escolher > 2):
            print("Escolher número 1 ou 2")

print()
print("Até breve")


