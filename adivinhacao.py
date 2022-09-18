import random


def jogar():

    jogar = True
    while jogar:

        numero_secreto = random.randrange(0, 9)
        total_de_tentativas = 3
        tentativa = 1
        acertou = False

        # Usando o For

        for rodada in range(1, total_de_tentativas + 1):
            print("Tente acertar o número secreto entre 0 e 9:")
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute = int(input("Digite seu chute: "))

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(maior):
                print("O número digitado é maior do que o número secreto.")
            elif(menor):
                print("O número digitado é menor do que o número secreto você tem ")
            elif(acertou):
                break
            tentativa = tentativa + 1

        # fiz esse bloco pois quando acerta não conta a tentativa quando acertou de ultima
        # foi realizado vários testes
        if(acertou):
            print("\nVocê acertou após " +
                  str(rodada) + " tentativas!")
        else:
            print("GAME OVER!\nO número secreto era " + str(numero_secreto) +
                  " e você não tem mais tentativas!")

        continuar = input("Deseja continuar jogando? (s/n): ")
        if continuar == 's':
            jogar = True
        else:
            jogar = False
        '''
        # Usando o While
        # Esse while roda sem precisar do break quando o usuário acerta
        while(total_de_tentativas > 0 and acertou == False):

            print("Tente acertar o número secreto entre 0 e 9:")
            print("\nTentativa {} de {}".format(tentativa, 3))
            chute = int(input("\nDigite seu chute: "))
            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(maior):
                print("\nO número digitado é maior do que o número secreto.")

            else:
                print("\nO número digitado é menor do que o número secreto você tem ")

            total_de_tentativas = total_de_tentativas - 1
            tentativa = tentativa + 1
            print("Você tem " + str(total_de_tentativas) + " tentativas:")

        if(acertou == False):
            print("GAME OVER!\nO número era " + str(numero_secreto) +
                " e você não tem mais tentativas!")
        else:
            print("\nVocê acertou após " +
                str(tentativas) + " tentativas!")
        '''
