
import types

x = (i for i in range(10))

if type(x) == types.GeneratorType:
  print("x is a GeneratorType")
else:
  print("x is not a GeneratorType")


