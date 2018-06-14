
import types

class foo:
  def method():
    return('a method')

f=foo()

x = f.fun

if type(x) == types.UnboundMethodType:
  print("x is a UnboundMethodType")
else:
  print("x is not a UnboundMethodType")


