
import types

x = xrange(1, 10)

if type(x) == types.XRangeType:
  print("x is a XRangeType")
else:
  print("x is not a XRangeType")


