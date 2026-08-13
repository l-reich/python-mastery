# stock.py

from structure import Structure


class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        """
        cossttiiinho#
        """
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


Stock.create_init()
