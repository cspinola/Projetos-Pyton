print("Olá Carlos \n Bom dia!")

mensagem = 'Oi Phyton!'

condicao = input("Você possui CNH?(s/n): \ns - para sim ou \nn - para não:\n")
if condicao == 's':
    print('Pode dirigir meu carro.')
else:
    print('Não encoste no meu veículo!!')


numero = input('Digite um número:\n')
print('O número digitado foi: ' + numero)
print('O número digitado foi: {}'.format(numero))

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

print('Seu nome é {} e sua idade é {}'.format(nome, idade))

bool(4 == 8/2)

while True:
    try:
        n = int(input('Digite um numero para calcular seu fatorial: '))
        if n < 0:
            print('Número deve ser maior ou igual a zero')
        else:
            break  # sai do loop
    except ValueError:
        print('Você não digitou um número')
