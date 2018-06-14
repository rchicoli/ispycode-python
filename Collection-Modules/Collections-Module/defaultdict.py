
from collections import defaultdict

str = 'mississippi'

d = defaultdict(int)
for key in str:
  d[key] += 1


print(d.items())


