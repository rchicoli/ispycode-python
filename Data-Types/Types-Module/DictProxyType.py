
import types

class Foo(object):
   pass

x = Foo.__dict__

if type(x) == types.DictProxyType:
  print("x is a DictProxyType")
else:
  print("x is not a DictProxyType")


