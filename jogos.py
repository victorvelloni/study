import adivinhacao
import forca

print("*****************************************")
print("******Bem vindo ao menu de jogos!********")
print("*****************************************\n")
print("(1) Jogo da Adivinhação\n(2) Jogo da Forca\n")
jogo_selecionado = int (input("Selecione uma das opções: "))

if (jogo_selecionado == 1):
    print("Você selecinou o Jogo da Adivinhação\n")
    adivinhacao.jogar()
if (jogo_selecionado == 2):
    print("Você selecinou o Jogo da Forca\n")
    forca.jogar()