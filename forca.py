
import random


def imprime_mensagem_abertura():
    print('******************************************')
    print('***Bem	vindo	ao	jogo	da	Forca!***')
    print('******************************************')


def carrega_palavra_secreta():
    palavras = []
    #arquivo = open('palavras.txt', 'r')
    with open('palavras.txt') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]  # .upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def jogar():
    imprime_mensagem_abertura()
    jogar = True
    palavras = []
    #arquivo = open('palavras.txt', 'r')

    while jogar:
        # palavra_secreta = random.choice(palavras)
        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavra_secreta = carrega_palavra_secreta()
        letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

        acertou = False
        enforcou = False
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
