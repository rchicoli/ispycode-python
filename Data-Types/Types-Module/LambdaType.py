
import types

x = lambda d:d*d

if type(x) == types.LambdaType:
  print("x is a LambdaType")
else:
  print("x is not a LambdaType")


