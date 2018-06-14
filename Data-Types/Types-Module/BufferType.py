
import types

x = buffer('Hello World')

if type(x) == types.BufferType:
  print("x is a BufferType")
else:
  print("x is not a BufferType")


