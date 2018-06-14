
import types

x = compile('2 + 2', '<string<', 'eval')

if type(x) == types.CodeType:
  print("x is a CodeType")
else:
  print("x is not a CodeType")


