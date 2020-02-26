
def jogar():
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = [ "_" , "_" , "_" , "_" , "_" , "_" ]
    ##palavra_secreta.capitalize() banana == Banana
    ##palavra_secreta.endswith("na") banana == true  palavra_secreta.endswith("naa") banana == false

    enforcou = False
    acertou  = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip(); #remover espaços.
        index = 0

        for letra in palavra_secreta:
            #if (chute.lower() == letra):
                #print(chute.lower())

            if (chute.upper() == letra.upper()):
                #print("Encontrei a letra {} na posição {}".format(letra, index + 1))
                letras_acertadas[index] = letra

            index = index + 1

        letras_faltando = str(letras_acertadas.count('_'))
        print()
        print("Ainda faltam acertas {} letras".format(letras_faltando))
        print(letras_acertadas)

        print("Jogando ...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

