
import types

x  = Ellipsis

if type(x) == types.EllipsisType:
  print("x is a EllipsisType")
else:
  print("x is not a EllipsisType")


