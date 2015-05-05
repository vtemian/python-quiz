class A(object):
    __slots__ = ['b']

    def __init__(self):
        self.a = 42
        self.b = 24


class B(A):
    pass

a = A()
try:
    a.b = 42
    a.a = 24
    a.c = 34
except Exception as exc:
    print("am prins o exceptie de tipul: {}".format(type(exc)))
else:
    print("am modificat a")


b = B()
try:
    b.b = 42
    b.a = 42
    b.c = 34
except Exception as exc:
    print("am prins o exceptie de tipul: {}".format(type(exc)))
else:
    print("am modificat b")
