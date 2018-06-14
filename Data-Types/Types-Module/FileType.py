
import types

x = open('example.py', 'r')

if type(x) == types.FileType:
  print("x is a FileType")
else:
  print("x is not a FileType")


