import forca
import adivinha

print("------------------------------------------------------")
print("                   Escolha seu Jogo                   ")
print("------------------------------------------------------")

print("(1) Jogo da Forca")
print("(2) Jogo de Adivinhação")

escolher_jogo = int(input('Selecionar jogo:'))

if(escolher_jogo == 1):
    print("Jogando Jogo da Forca")
    forca.jogar()
elif(escolher_jogo == 2):
    print("Jogando Jogo de Adivinhação")
    adivinha.jogar()