
import types
import sys

a=b=c=None

try:
  1/0
except:
  a,b,c = sys.exc_info()
  print(a)
  print(b)
  print(c)

if type(c) == types.TracebackType:
  print("c is a TracebackType")
else:
  print("c is not a TracebackType")


