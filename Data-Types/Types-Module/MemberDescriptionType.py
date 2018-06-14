
import types
import datetime

x = datetime.timedelta.days

if type(x) == types.MemberDescriptorType:
  print("x is a MemberDescriptorType")
else:
  print("x is not a MemberDescriptorType")


