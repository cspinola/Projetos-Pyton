print(' Jogo da adivinhação')
nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

print('Seu nome é {} e sua idade é {}'.format(nome, idade))
numero_secreto = 9
print("Tente acertar o número inteiro de 0 a 10!\n")
chute_str = int(input("Digite seu número:\n"))


while (chute_str != numero_secreto):
    if (chute_str > numero_secreto):
        print("Seu número é maior do que o número secreto!\n")
        chute_str = int(input("Digite outro número:\n"))
    elif (chute_str < numero_secreto):
        print("Seu número é maior do que o número secreto!\n")
        chute_str = int(input("Digite outro número:\n"))

print("Você acertou o número secreto é " + numero_secreto)
