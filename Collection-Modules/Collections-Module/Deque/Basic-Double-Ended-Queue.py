
import collections

d = collections.deque('abcdefg')
print('Deque    : %s' % d)
print('Length   : %s' % len(d))
print('Left end : %s' % d[0])
print('Right end: %s' % d[-1])

d.remove('d')
print('remove(d): %s' % d)


