
import types

x = len

if type(x) == types.BuiltinFunctionType:
  print("x is a BuiltinFunctionType")
else:
  print("x is not a BuiltinFunctionType")


