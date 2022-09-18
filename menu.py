import adivinhacao
import forca

print('*********************************')
print('**********MENU	DE	JOGOS**********')
print('*********************************')
print('1 - Adivinhação')
print('2 - Forca')
print('0 - Sair')
jogo_escolhido = int(input('Qual jogo quer jogar? \nDigite um número: '))

if jogo_escolhido == 1:
    adivinhacao.jogar()
elif jogo_escolhido == 2:
    forca.jogar()
elif jogo_escolhido != 1 | 2:
    quit()
