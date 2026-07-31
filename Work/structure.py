import sys
import inspect


class Structure:
    _fields = ()

    @classmethod
    def create_init(cls):
        argstr = ",".join(cls._fields)
        code = f"def __init__(self, {argstr}):\n"
        for name in cls._fields:
            code += f"    self.{name} = {name}\n"

        locs = {}
        exec(code, locs)
        cls.__init__ = locs["__init__"]

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
