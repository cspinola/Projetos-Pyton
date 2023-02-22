import history

class Account:

    def __init__(self, number, owner, balance=0.0, limit=1000.0):
        self.owner = Client
        self.number = number
        self.balance = balance
        self.limit = limit
        self.history = accountStatement()
        #self.adress = []

    # def addAdress(self, street, postalcode, number, type):
     #   self.adress.append(Adress(street, postalcode, number, type))

    def deposit(self, value):
        self.balance += value
        self.history.transactions.append("deposit of $ {}".format(value))

    def withdraw(self, value):

        if (self.balance < value):
            return False
        else:
            self.balance -= value
            self.history.transactions.append("withdraw of $ {}".format(value))
            return True

    def tansfer(self, destiny, value):
        enought_balance = withdraw(self, value)
        if(enought_balance == False):
            return False
        else:
            deposit(destiny, value)
            self.history.transactions.append(
                "transfer of $ {} to {}".format(value, destiny))
            return True

    def accountprint(self):
        print('number: {}\nholder: {}\nbalance:'.format(
            self.number, self.holder, self.balance))


class Client:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id
        # self.adress


class Adress():
    def __init__(self, street, number, postalcode, type='home'):
        self.street = street
        self.postalcode = postalcode
        self.number = self.add_number(number)
        self.type = type

    def add_number(self, number):
        if(number.isnumeric()):
            self.number = number
        else:
            self.number = 0

    def __str__(self):
        return f'Street: {self.street} - n.o: {self.number} - Cpl: {self.type} - postalcode: {self.postalcode} '


# Tests
cliente = Client('João', 'Oliveira', '1111111111-1')
minha_conta = Account('123-4', 120.0, 1000.0)
minha_conta.owner = cliente
print(cliente.name)
print(minha_conta.owner.name)
print(minha_conta.balance)

cliente2 = Client('José', 'Amaral', '1111111111-3')
minha_conta2 = Account('333-4', cliente2, 400.0, 1000.0)
#minha_conta.owner = cliente
print(cliente2.name)
print(minha_conta2.owner.name)
print(datetime.datetime.today())
