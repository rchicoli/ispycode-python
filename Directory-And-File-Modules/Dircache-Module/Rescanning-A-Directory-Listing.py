
import dircache
import os

path = '/tmp'
newfile = os.path.join(path, 'file1.txt')

# directory contents
list1 = dircache.listdir(path)

# rescan the directory
list2 = dircache.listdir(path)

print 'Identical :', list1 is list2
print 'Equal     :', list1 == list2
print 'Difference:', list(set(list2) - set(list1))

# create the new file
open(newfile, 'wt').close()

# rescan the directory
list3 = dircache.listdir(path)

# remove new file
os.unlink(newfile)

print 'Identical :', list1 is list3
print 'Equal     :', list1 == list3
print 'Difference:', list(set(list3) - set(list1))


