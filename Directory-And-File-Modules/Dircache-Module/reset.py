
import dircache

path = '/tmp'
list1 = dircache.listdir(path)
list2 = dircache.listdir(path)

print 'Identical :', list2 is list1
print 'Equal     :', list2 == list1

dircache.reset()

list3 = dircache.listdir(path)
print 'Identical :', list3 is list1
print 'Equal     :', list3 == list1


