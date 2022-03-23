
def jogar():

    import random

    print("-----------------------------------------------------")
    print("          Bem Vindo ao Jogo de Adivinhação!          ")
    print("-----------------------------------------------------")
    numero_secreto = round(random.randrange(1, 101))
    numero_de_tentativas = 0
    pontos = 1000

    print("Escolha a dificuldade do jogo")
    print("(1) -   Facil, 20 chances")
    print("(2) -   Medio, 10 chances")
    print("(3) - Dificil, 05 chances")
    nivel = int(input("Defina a dificuldade: "))

    if(nivel == 1):
        numero_de_tentativas = 20
    elif(nivel == 2):
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5

    for rodada in range (1, numero_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, numero_de_tentativas))
        chute = int(input("Digite sua Especulação entre 1 e 100:"))

        if(chute < 1 or chute > 100):
            print("As especulações devem ser entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou")
            print("Pontos totais: {}".format(pontos))
            break
        else:
            if(maior):
                print("Vish, passou perto! O chute foi maior.")
            elif(menor):
                print("Vish, passou perto! O chute foi menor.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo!!!")

if(__name__ == "__main__"):
    jogar()