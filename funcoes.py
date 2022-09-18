def velocity(distance, time):
    return distance/time

def dados(name, age=None):
    if(age is not None):
        return ('Name: {} \n age: {}'.format(name, age))
    else:
        return ('Name: {} age was not informed.'.format(name))


print(velocity(100, 50))
print(dados('João', 23))


def soma(x, y):
    return{'a soma é': x+y}


def subtracao(x, y):
    return{'a subtracao é': x-y}


def calculadora(x, y):

    return {soma(x, y), subtracao(x, y)}
    print('Soma é {} e a subtração é {}'.format(soma(x, y), subtracao(x, y)))


def divisao(a, b):
    return a/b


def velocidade_media(a, b):
    return divisao(a, b)


print('A velocidade média foi: {}'.format(velocidade_media(3, 2)))

#print((calculadora(10, 5)))

#resultados = calculadora(1, 2)

# for key in resultados:
#    print('{}:	{}'.format(key,	resultados[key]))


def teste(arg, *args):
    print('primeiro	argumento:	{}'.format(arg))
    for arg in args:
        print('proximo	argumento:	{}'.format(arg))


teste('fi', 'duma', 'égua', 3.14)
