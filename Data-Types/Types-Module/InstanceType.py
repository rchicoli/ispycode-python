
import types

class foo:
  bar = 'hello'

x=foo()

if type(x) == types.InstanceType:
  print("x is a InstanceType")
else:
  print("x is not a InstanceType")


