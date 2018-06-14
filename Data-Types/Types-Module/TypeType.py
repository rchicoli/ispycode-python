
import types

x = type(1)

if type(x) == types.TypeType:
  print("x is a Type")
else:
  print("x is not a Type")


