
import types
import inspect

x = inspect.currentframe()

if type(x) == types.FrameType:
  print("x is a FrameType")
else:
  print("x is not a FrameType")


