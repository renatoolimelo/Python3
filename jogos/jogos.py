print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Informe o jogo escolhido: "))

if (jogo == 1):
    print("Jogando forca")
elif (jogo == 2):
    print("Jogando adivinhação")
else:
    print("Escolha invalida")
