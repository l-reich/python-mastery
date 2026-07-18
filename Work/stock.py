import csv


class Stock:
    _types = (str, int, float)
    __slots__ = ("name", "_shares", "_price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, val):
        specified_type = Stock._types[1]
        if not isinstance(val, specified_type):
            raise ValueError
        if val < 0:
            raise ValueError
        self._shares = val

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        specified_type = Stock._types[2]
        if not isinstance(val, specified_type):
            raise ValueError
        if val < 0:
            raise ValueError
        self._price = val

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt

    @classmethod
    def from_row(cls, row: list[str]):
        vals = (func(val) for func, val in zip(cls._types, row))
        return cls(*vals)


def print_portfolio(portfolio: list[Stock]) -> None:
    for s in portfolio:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))
