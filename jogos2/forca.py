import random

def jogar():

    imprime_bem_vindo()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    letras_chutadas = []
    tentativa = 1
    tentativas_max = 6

    while (not enforcou and not acertou):

        acertou_a_letra = False

        imprime_tentativas(tentativa, tentativas_max, letras_acertadas, letras_chutadas)

        chute = input("Letra escolhida: ").upper().strip()

        if (chute in letras_chutadas or chute in letras_acertadas):
            print("Você já tentou essa letra!")
            continue

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
                acertou_a_letra = True
            index += 1

        if (not acertou_a_letra):
            letras_chutadas.append(chute)
            letras_chutadas.sort()
            tentativa += 1

        falta_letras = "_" in letras_acertadas

        if (not falta_letras):
            print("Você ganhou!")
            acertou = True

        if (tentativa > tentativas_max):
            print("Você perdeu!")
            print("Letras chutadas: {}".format(letras_chutadas))
            print(letras_acertadas)
            enforcou = True

    print("Palavra secreta: {}".format(palavra_secreta))
    print()
    print("Fim do jogo")

def imprime_bem_vindo():
    print("********************************")
    print("***Bem vindo ao jogo de forca***")
    print("********************************")
    print("")

def carrega_palavra_secreta():
    palavras = []
    with open("/home/renato/Git/Python3/jogos2/palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().upper())

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    letras_acertadas = ["_" for letra in palavra_secreta]
    return letras_acertadas

def imprime_tentativas(tentativa, tentativas_max, letras_acertadas, letras_chutadas):
    print("Chute {} de {}".format(tentativa, tentativas_max))

    if (tentativa > 1):
        print()
        print("Letras chutadas: {}".format(letras_chutadas))
        print()

    print(letras_acertadas)
    print()

if (__name__ == "__main__"):
    jogar()



