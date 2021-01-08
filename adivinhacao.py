import random

print("*****************************************")
print("****Bem vindo ao jogo de adivinhação!****")
print("*****************************************\n")
print("Digite o número da dificuldade você deseja")
dific = int(input("(1) Fácil | (2) Médio | (3) Difícil\n"))

if dific == 1:
    num_tentativas = 15
elif dific == 2:
    num_tentativas = 10
else:
    num_tentativas = 5

pontos = 500
num_secreto = random.randrange(1, 101)
rodada = 1

for rodada in range(rodada, num_tentativas+1):
    print("\nTentativa {} de {}".format(rodada, num_tentativas))
    chute = int(input("Digite um número: "))
    acertou = (chute == num_secreto)
    maior = chute > num_secreto

    if(acertou):
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!Parabéns! Você acertou o número!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

        print("Você fez {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("Seu número é maior que o número correto\n")
            print("***************************************\n")
            if (rodada == num_tentativas):
                print("\nVocê perdeu! :(\nO número secreto era {}. Você fez {} pontos.".format(num_secreto, pontos))
        else:
            print("Seu número é menor que o número correto\n")
            print("***************************************\n")
            if (rodada == num_tentativas):
                print("\nVocê perdeu! :(\nO número secreto era {}. Você fez {} pontos.".format(num_secreto, pontos))
            
            pontos_perdidos = abs(num_secreto - chute)
            pontos = pontos - pontos_perdidos 

print("Fim do jogo!")