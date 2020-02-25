print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

#if (numero_secreto == chute):
#    print("Você acertou")
#else:
#    print("Você errou")

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou")
elif (maior):
    print("Você errou! O seu chute foi maior do que o número secreto")
elif(menor):
    print("Você errou! O seu chute foi menor do que o número secreto")

print("Fim do jogo")

###########################################################

numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)
##resultado 20202020202020202020