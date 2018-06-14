
import types
import datetime

x = datetime

if type(x) == types.ModuleType:
  print("x is a ModuleType")
else:
  print("x is not a ModuleType")


