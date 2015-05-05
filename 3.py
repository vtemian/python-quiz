class Foo(object):
   a = 1


foo = Foo()
foo.a = 2
Foo.a = 3
print(foo.a)
print(type(foo).a)
