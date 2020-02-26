import random

def jogar():
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    ##arquivo = open("palavras.txt", "r") r - leitura, a - adição - w - escrita
    ##arquivo = open("palavras.txt", "r") leitura do arquivo
    ##arquivo.close() fecha o arquivo

    ##for letra in palavra_secreta:
    ##    letras_acertadas.append("_")

    ##palavra_secreta.capitalize() banana == Banana

    ##palavra_secreta.endswith("na") banana == true  palavra_secreta.endswith("naa") banana == false

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

if(__name__ == "__main__"):
    jogar()

