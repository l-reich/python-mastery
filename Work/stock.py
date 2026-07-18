import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt

def read_portfolio(fn: str) -> list[Stock]:
    res_list = []
    with open(fn, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            res_list.append(Stock(str(row[0]), int(row[1]), float(row[2])))

    return res_list

def print_portfolio(portffolio: list[Stock]) -> None:
    for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
