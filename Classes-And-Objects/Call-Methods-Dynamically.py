
class Foo(object):
  def a(self):
     print("A")
  def b(self):
     print("B")

foo = Foo()
funa = getattr(foo, 'a')
funb = getattr(foo, 'b')
funa()
funb()


