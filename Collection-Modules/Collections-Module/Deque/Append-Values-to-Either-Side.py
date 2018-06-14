
from collections import deque

d = deque(['a','b','c'])
print(d)

# append to the left
d.appendleft('z')
print(d)

# append to the right
d.append('q')
print(d)


