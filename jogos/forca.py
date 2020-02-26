
def jogar():
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    ##palavra_secreta.capitalize() banana == Banana
    ##palavra_secreta.endswith("na") banana == true  palavra_secreta.endswith("naa") banana == false

    enforcou = False
    acertou  = False


    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip(); #remover espaços.
        index = 0

        for letra in palavra_secreta:
            #if (chute.lower() == letra):
                #print(chute.lower())

            index = index + 1
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))

        print("Jogando ...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

