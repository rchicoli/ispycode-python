
import types

def x():
  return "hello"

if type(x) == types.FunctionType:
  print("x is a FunctionType")
else:
  print("x is not a FunctionType")


