
import types

x = u'hello'

if type(x) == types.UnicodeType:
  print("x is a Unicode")
else:
  print("x is not a Unicode")


