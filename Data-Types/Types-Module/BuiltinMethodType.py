
import types
from datetime import date

x = date.today

if type(x) == types.BuiltinMethodType:
  print("x is a BuiltinMethodType")
else:
  print("x is not a BuiltinMethodType")


