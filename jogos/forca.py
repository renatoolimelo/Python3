import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou  = False
    tentativas = 6

    while(not enforcou and not acertou):

        chute = pede_chute()
        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas -= 1
            print()
            print("Ops, você errou! Restam {} tentativas!".format(tentativas))
        if("_" in letras_acertadas):
            letras_faltando(letras_acertadas)
        else:
            venceu_jogo(letras_acertadas)
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

def pede_chute():
    chute = input("Qual letra? ")
    return chute.strip().upper()

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    print()
    print("Você acertou!")

def letras_faltando(letras_acertadas):
    letras_faltando = str(letras_acertadas.count('_'))
    print()
    print("Ainda faltam acertas {} letras".format(letras_faltando))
    print(letras_acertadas)
    print()

def venceu_jogo(letras_acertadas):
    print(letras_acertadas)
    print("Você ganhou!")

if(__name__ == "__main__"):
    jogar()