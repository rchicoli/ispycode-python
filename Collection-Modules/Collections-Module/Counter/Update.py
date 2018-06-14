
from collections import Counter

c = Counter(a=10, b=7, c=3)
print(c)
d = Counter(a=3, b=2, c=1)
print(d)

c.update(d)
print(c)


