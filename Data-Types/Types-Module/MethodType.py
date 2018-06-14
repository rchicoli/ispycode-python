
import types

class foo:
  def method():
    return('a method')

f=foo()

x = f.fun

if type(x) == types.MethodType:
  print("x is a MethodType")
else:
  print("x is not a MethodType")


