import datetime


class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('data de abertura: {}'.format(self.data_abertura))
        print('transacoes: ')
        for t in self.transacoes:
            print('-', t)
