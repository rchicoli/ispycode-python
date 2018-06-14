
import types

a = str('hello')
b = unicode(u'world')

print(type(a))

if isinstance(a, types.StringTypes):
  print("a is a StringTypes")

print(type(b))

if isinstance(b, types.StringTypes):
  print("b is a StringTypes")


