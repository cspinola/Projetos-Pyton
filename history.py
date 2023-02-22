import datetime


class history:  # accountStatement
    def __init__(self):
        self.openDate = datetime.datetime.today()
        self.transactions = []

    def imprime(self):
        print("Open Date: {}".format(self.openDate))
        print("transactions: ")
        for t in self.transactions:
            print("-", t)