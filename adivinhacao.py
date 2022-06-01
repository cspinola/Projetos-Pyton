import random
numero_secreto = random.randrange(0, 9)
total_de_tentativas = 3

print("Tente acertar o número secreto entre 0 e 9:")
chute = int(input("\nDigite seu chute: "))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

while(total_de_tentativas > 0 and acertou == False):

    if(maior):
        chute = int(input("\nO número digitado é maior do que o número secreto você tem " +
                          str(total_de_tentativas) + " tentativas:"))

    else:
        chute = int(input("\nO número digitado é menor do que o número secreto você tem " +
                          str(total_de_tentativas) + " tentativas:"))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    total_de_tentativas = total_de_tentativas - 1

if(acertou == False):
    print("GAME OVER!\nO número era " + str(numero_secreto) +
          "\nVocê não tem mais tentativas!")
else:
    print("\nVocê acertou após " +
          str(4 - total_de_tentativas) + " tentativas!")
