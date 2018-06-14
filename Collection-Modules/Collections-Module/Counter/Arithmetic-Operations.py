
from collections import Counter

c1 = Counter(a=10, b=10, c=10)
print(c1)

c2 = Counter(a=1, b=2, c=3)
print(c2)

c3 = (c1 + c2)
print(c3)

c4 = (c1 - c2)
print(c4)


