from types import ModuleType


class Dummy():
    def __init__(self, *args, **kwargs):
        self.___dict = {}

    def __add__(self, other):
        return Dummy()

    def __sub__(self, other):
        return Dummy()

    def __mul__(self, other):
        return Dummy()

    def __truediv__(self, other):
        return Dummy()

    def __floordiv__(self, other):
        return Dummy()

    def __mod__(self, other):
        return Dummy()

    def __pow__(self, other, modulo=None):
        return Dummy()

    def __lshift__(self, other):
        return Dummy()

    def __rshift__(self, other):
        return Dummy()

    def __and__(self, other):
        return Dummy()

    def __xor__(self, other):
        return Dummy()

    def __or__(self, other):
        return Dummy()

    def __iadd__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __idiv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __imod__(self, other):
        pass

    def __ipow__(self, other, modulo=None):
        pass

    def __ilshift__(self, other):
        pass

    def __irshift__(self, other):
        pass

    def __iand__(self, other):
        pass

    def __ixor__(self, other):
        pass

    def __ior__(self, other):
        pass

    def __neg__(self):
        return Dummy()

    def __pos__(self):
        return Dummy()

    def __abs__(self):
        return Dummy()

    def __invert__(self):
        return Dummy()

    def __complex__(self):
        return 1 + 0j

    def __int__(self):
        return 1

    def __long__(self):
        return 1

    def __float__(self):
        return 1.0

    def __oct__(self):
        return oct(1)

    def __hex__(self):
        return hex(1)

    def __lt__(self, other):
        return True

    def __le__(self, other):
        return True

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __getattr__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            dummy = Dummy()
            setattr(self, attr, dummy)
            return dummy

    def __getitem__(self, key):
        if key in self.___dict:
            return self.___dict[key]
        dummy = Dummy()
        self.___dict[key] = dummy
        return dummy

    def __setitem__(self, key, value):
        self.___dict[key] = value

    def __call__(self, *args, **kwargs):
        return Dummy()

    def __len__(self):
        return 1

    def __str__(self):
        return ""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is None


class DummyModule(Dummy, ModuleType):
    pass
