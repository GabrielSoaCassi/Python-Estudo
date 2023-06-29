import forca
import  advinhacao
print("*********************************")
print("******Escolha o seu Jogo!******")
print("*********************************")
print("(1) Forca (2) Adivinhação")

escolha_jogo = int(input("Qual Jogo deseja escolher ?\n"))

if(escolha_jogo == 1):
    print("Jogo da Forca")
    forca.jogar()
else:
    print("Jogo da Adivinhação")
    advinhacao.jogar()