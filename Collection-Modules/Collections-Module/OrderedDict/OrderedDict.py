
from collections import OrderedDict

# regular unsorted dictionary
d1 = &#123;'c':10,'a':20,'d':30,'b':40&#125;

# sorted by key
d2 = OrderedDict(sorted(d1.items(), key=lambda t: t[0]))
print(d2)

# sorted by value
d3 = OrderedDict(sorted(d1.items(), key=lambda t: t[1]))
print(d3)


