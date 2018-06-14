
import types
import array

x = array.array.typecode

if type(x) == types.GetSetDescriptorType:
  print("x is a GetSetDescriptorType")
else:
  print("x is not a GetSetDescriptorType")


