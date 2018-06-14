
import types

x = 2 + 3j

if type(x) == types.ComplexType:
  print("x is a Complex")
else:
  print("x is not a Complex")


