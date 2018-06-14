
import bisect
import random

l = []
for i in range(1, 20):
  r = random.randint(1, 20)
  pos = bisect.bisect_right(l, r)
  bisect.insort_right(l, r)
  print '%2d %2d' % (r, pos), l


