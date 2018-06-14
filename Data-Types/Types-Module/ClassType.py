
import types

class x:
  i = 10

if type(x) == types.ClassType:
  print("x is a ClassType")
else:
  print("x is not a ClassType")


