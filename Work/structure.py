import sys
import inspect


class Structure:
    _fields = ()

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple((str(s) for s in sig.parameters))

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs["self"]
        for name, val in locs.items():
            if name == "self":
                continue
            setattr(self, name, val)

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
