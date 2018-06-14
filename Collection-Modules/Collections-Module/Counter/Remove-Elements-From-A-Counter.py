from collections import Counter

c = Counter(x=10, y=7, z=3)
print(c)

c['z'] = 0
print(c)

del c['z']
print(c)


