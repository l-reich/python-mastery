class Structure:
    _fields = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected %d arguments" % len(self._fields))
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)

    def __repr__(self):
        classname = self.__class__.__name__
        arg_string = ", ".join(
            str(getattr(self, attr_name)) for attr_name in self._fields
        )
        return f"{classname}({arg_string})"

    def __setattr__(self, attr_name, value):
        if attr_name[0] == "_":
            super().__setattr__(attr_name, value)
            return
        if attr_name not in self._fields:
            raise AttributeError("No attribute %s" % attr_name)

        super().__setattr__(attr_name, value)


class Stock(Structure):
    _fields = ("name", "shares", "price")


class Date(Structure):
    _fields = ("year", "month", "day")
