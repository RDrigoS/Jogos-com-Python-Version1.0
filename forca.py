
import random

def jogar():

    apresentacao_do_jogo()
    palavra_secreta = seleciona_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while not enforcou and not acertou:

        print('Você usou {} de 7 tentativas'.format(tentativas))
        chute = solicita_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)
        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def apresentacao_do_jogo():
    print('-----------------------------------------------------')
    print('             Bem Vindo ao Jogo de Forca!             ')
    print('-----------------------------------------------------')
    # exibe ao usuário a apresentação do jogo da forca

def seleciona_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close
    # busca no arquivo palavras.txt uma palavra para ser usada no jogo, apos selecionada ele fecha o arquivo

    numero = random.randrange(0, len(palavras)) # faz a contagem de palavras existentes no arquivo e seleciona uma palavra aleatoria
    palavra_secreta = palavras[numero].upper() # pega a palavra e transforma ela em letras maiusculas maca -> MACA
    return palavra_secreta # retorna a palavra para a variavel "palavra_secreta"

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta] # ele pega a palavra_secreta e transforma e "_" ex: MACA -> '_','_','_','_' e retorna a palavra_secreta

def solicita_chute():
    chute = input('Digite uma letra: ') # exibe ao usuario a socilitação da letra para o chute
    chute = chute.strip().upper() # o strip() remove os espaços em branco e o upper() letras maiusculas "  b  " -> "B"
    return chute # retorna a resposta para a variavel chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == '__main__':
    jogar()