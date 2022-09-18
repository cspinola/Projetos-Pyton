
import random


def jogar():
    print('******************************************')
    print('***Bem	vindo	ao	jogo	da	Forca!***')
    print('******************************************')

    jogar = True

    while jogar:
        plavras = ['banana', 'palavra', 'escova',
                   'chave', 'caneta', 'prato', 'papel', 'comida']
        palavra_secreta = random.choice(plavras)
        # palavra_secreta = 'banana'

        acertou = False
        enforcou = False

        letras_acertadas = []
        for i in palavra_secreta:
            letras_acertadas.append('_')

        erros = 0

        print('Tente acertar a Palavra!\n Você possui 6 tentativas no caso a letra digitada não faça parte da palavra secreta.')

        while (not acertou and not enforcou):
            chute = input('Digite uma letra:')

            if (chute in palavra_secreta):

                posicao = 0

                for letra in palavra_secreta:
                    if (chute.upper() == letra.upper()):
                        print('Encontrei a letra {} na posição {}'.format(
                            letra, posicao))
                        letras_acertadas[posicao] = letra
                    posicao += 1

            else:
                erros += 1
                print('Essa letra não faz parte da palavra secreta, você tem {} tentativas'.format(
                    6-erros))

            acertou = '_' not in letras_acertadas
            enforcou = erros == 6
            print(letras_acertadas)
        # print('Você errou {} sendo o máximo de 6'.format(erros))

        if (acertou):
            print('Parabéns! Você acertou! A palavra secreta era {}.'.format(
                palavra_secreta))
        else:
            print('Você perdeu o jogo! A palavra secreta era {}.'.format(
                palavra_secreta))

        continuar = input("Deseja continuar jogando? (s/n): ")

        if continuar == 's':
            jogar = True
        else:
            jogar = False

    print('Fim do Jogo!!!')
