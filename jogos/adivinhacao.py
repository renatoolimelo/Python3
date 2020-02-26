import random

#https://docs.python.org/3/library/string.html#formatexamples - exemplos de formatação

print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

#numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
rodada = 1

#print(numero_secreto)

##while (rodada <= total_de_tentativas ):
for rodada in range (1,total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")

    print("Você digitou ", chute_str)

    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um núemro entre 1 e 100!")
        continue

    # if (numero_secreto == chute):
    #    print("Você acertou")
    # else:
    #    print("Você errou")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    elif (maior):
        print("Você errou! O seu chute foi maior do que o número secreto")
    elif (menor):
        print("Você errou! O seu chute foi menor do que o número secreto")

print("Fim do jogo")

###########################################################

#numero1 = 10
#numero2 = "20"
#produto = numero1 * numero2
#print(produto)
##resultado 20202020202020202020
