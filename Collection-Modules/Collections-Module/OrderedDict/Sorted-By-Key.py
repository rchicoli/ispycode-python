
from collections import OrderedDict

# regular unsorted dictionary
d1 = {'c':10,'a':20,'d':30,'b':40}
print(d1)

# sorted by key
d2 = OrderedDict(sorted(d1.items(), key=lambda t: t[0]))
print(d2)


