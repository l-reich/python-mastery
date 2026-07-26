from validate import PositiveInteger, PositiveFloat, String


class Stock:
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()
    #_types = [String, PositiveInteger, PositiveFloat]
    _types = [str, int, float]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, val):
        self._shares = PositiveInteger.check(val)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        self._price = PositiveFloat.check(val)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt

    def __repr__(self):
        return "Stock('%s', %s, %s)" % (self.name, self.shares, self.price)

    @classmethod
    def from_row(cls, row: list[str]):
        vals = (func(val) for func, val in zip(cls._types, row))
        return cls(*vals)

    def __eq__(self, other):
        return isinstance(other, Stock) and (
            (self.name, self.shares, self.price)
            == (other.name, other.shares, other.price)
        )


def print_portfolio(portfolio: list[Stock]) -> None:
    for s in portfolio:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))
