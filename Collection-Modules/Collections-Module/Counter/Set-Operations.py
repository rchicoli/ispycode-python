
from collections import Counter

c1 = Counter(a=10, b=9, c=8)
print(c1)

c2 = Counter(b=8, c=7, d=6)
print(c2)

# Intersection
c3 = (c1 & c2)
print(c3)

# Union
c4 = (c1 | c2)
print(c4)


