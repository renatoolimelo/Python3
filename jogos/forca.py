import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou  = False
    tentativas = 6

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()     #remover espaços, e deixar tudo maiusculo

        if (chute in palavra_secreta):

            index = 0

            for letra in palavra_secreta:
                #if (chute.lower() == letra):
                    #print(chute.lower())

                if (chute == letra):
                    #print("Encontrei a letra {} na posição {}".format(letra, index + 1))
                    letras_acertadas[index] = letra

                index += 1

            print()
            print("Você acertou!")

        else:

            tentativas -= 1
            print()
            print("Ops, você errou! Restam {} tentativas!".format(tentativas))

        if("_" in letras_acertadas):

            letras_faltando = str(letras_acertadas.count('_'))
            print()
            print("Ainda faltam acertas {} letras".format(letras_faltando))
            print(letras_acertadas)
            print()

        else:
            print(letras_acertadas)
            print("Você ganhou!")
            break

        enforcou = tentativas == 0

    if(enforcou):
        print("Você perdeu!")

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

if(__name__ == "__main__"):
    jogar()