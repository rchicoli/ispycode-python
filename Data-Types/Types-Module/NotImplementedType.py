
import types

def fun():
   return NotImplemented

x = fun()

if type(x) == types.NotImplementedType:
  print("x is a NotImplementedType")
else:
  print("x is not a NotImplementedType")


