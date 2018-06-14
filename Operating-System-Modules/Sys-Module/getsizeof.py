
import sys

class Foo(object):
  def a(self):
     print("A")
  def b(self):
     print("B")

f = Foo()
print(sys.getsizeof(f))


