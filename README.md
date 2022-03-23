# Jogos_com_Python

Esse projeto foi desenvolvido juntamente com a plataforma de ensino da Alura

Jogos:
 - Central que e possível escolher o jogo a ser jogado

Jogo do adivinha:
 - Pede para o usuário escolher o nível de dificuldade desejado, logo após e determinado o numero secreto junto com a quantidade de chances baseado na dificuldade.
 - Cada chute do usuário passa por uma verificação, caso o numero seja correto ele para com o jogo e exibe a mensagem para o vencedor junto com a pontuação. Se as chances se esgotam, e exibido a mensagem que o jogador perdeu. 

Jogo da Forca:
 - A palavra e selecionada aleatoriamente através de um arquivo que o Python faz a leitura, e mantida em segredo com "_" mostrando a quantidade de letras que a palavra contem
 - Cada tentativa do usuário passa pela verificação, caso a letra contenha na palavra secreta, no lugar dos "_" e subsistido pela letra informada. Se a letra estiver incorreta, e exibido um feedback visual e texto mostrando para o usuário as chances e forca
 - Quando o jogo chega ao final, seja por falta de tentativa ou palavra completa e mostrado um feedback visual e texto
