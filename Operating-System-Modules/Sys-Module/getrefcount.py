
import sys

class Foo(object):
  def a(self):
     print("A")

f1 = Foo()
f2 = f1
f3 = f2

print(sys.getrefcount(f1))


