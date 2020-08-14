import random

print("Bem vindo ao jogo de adivinhação!")

numero_secreto = random.randrange(1,101)
dificuldade = 0
total_de_pontos = 1000
#rodada = 1

while (dificuldade < 1 or dificuldade > 3):
    print("Escolha seu nível:")
    print("1 - Fácil")
    print("2 - Intermediario")
    print("3 - Dificil")
    dificuldade = int(input("Escolha:"))

    if (dificuldade < 1 or dificuldade > 3):
        print("Esolher um nível de 1 a 3")
        continue

    if (dificuldade == 1):
        total_de_tentativas = 10
    elif (dificuldade == 2):
        total_de_tentativas = 8
    else:
        total_de_tentativas = 4

print("")
print("Prêmio do jogo R$ {:08.2f}".format(123.9))
print("Pontuação {:d}".format(total_de_pontos))

#while (rodada <= total_de_tentativas):
for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = 0
    while (chute < 1 or chute > 100):
        chute = int(input("Digite um número entre 1 e 100:"))

        if (chute < 1 or chute > 100):
            print("Número inválido. Escolher número entre 1 e 100!")


    print ("Seu número é", chute)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Você acertou!")
        print("Pontuação {:d}".format(total_de_pontos))
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        total_de_pontos = total_de_pontos - pontos_perdidos
        print("")
        if(maior):
            print("Você chutou um número maior")
        else:
            print("Você chutou um número menor")

    #rodada += 1
    print()

print("Fim do jogo número secreto: {}".format(numero_secreto))

