class Conta:
    pass

    def __init__(self, numero, cliente, saldo, limite=1000):
        print('Inicializando Conta')
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append('depósito de {}'.format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append('saque de {}'.format(valor))
            return True

    def extrato(self):
        print('numero: {} \nsaldo: {}'.format(self.numero, self.saldo))

    def transfere(self, destino, valor):
        retiirou = self.saca(valor)
        if(retirou):
            return False
        else:
            destino.deposita(valor)
            return True


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


def main():
    conta1 = Conta(1, "Zé", 1555, 2000)
    print(conta1.saldo)
    print(conta.titular.nome)
    extrato(conta1)


main()
