
import sys

def function():
  x = 1/0

try:
  function()
except:
  exc_type, exc_value, exc_tb = sys.exc_info()
  print("Type:      %s " % exc_type)
  print("Exception: %s " % exc_value)
  print("Traceback: %s " % exc_tb)


