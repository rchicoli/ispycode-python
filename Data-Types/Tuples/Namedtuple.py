
import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=18)
tom = Person(name='Tom', age=40)
bill = Person(name='Bill', age=22)

for p in [ bob, tom, bill ]:
    print 'Name:%s  Age:%d' % p


