
import bisect
import random

l = []
for i in range(1, 20):
  r = random.randint(1, 20)
  pos = bisect.bisect_left(l, r)
  bisect.insort_left(l, r)
  print '%2d %2d' % (r, pos), l


