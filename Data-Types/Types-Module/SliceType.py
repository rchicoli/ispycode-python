
import types

x  = slice(0, 5, 2)

if type(x) == types.SliceType:
  print("x is a SliceType")
else:
  print("x is not a SliceType")


