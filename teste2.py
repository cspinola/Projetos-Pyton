
import random

plavras = ['banana', 'palavra', 'escova', 'azul',
           'chave', 'caneta', 'prato', 'papel', 'comida']
jogar = True


def selectRandom(plavras):
    return random.choice(plavras)


palavra_secreta = selectRandom(plavras)  # random.choice(plavras)

letras_acertadas = []
for i in palavra_secreta:
    letras_acertadas.append('_')

#print("The name selected is: ", selectRandom(plavras))
print(palavra_secreta)
print((palavra_secreta.__sizeof__()))

print(letras_acertadas)
