print("Bem vindo ao jogo de adivinhação!")

numero_secreto = 42
total_de_tentativas = 3
#rodada = 1

#while (rodada <= total_de_tentativas):
for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = 0
    while (chute < 1 or chute > 100):
        chute = int(input("Digite um número entre 1 e 100:"))

        if (chute < 1 or chute > 100):
            print("Número inválido. Escolher número entre 0 e 100!")


    print ("Seu número é", chute)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    elif(maior):
        print("Você chutou um número maior")
    else:
        print("Você chutou um número menor")

    #rodada += 1
    print()

print("fim do jogo")




