
import fnmatch
import os

pattern = '*.txt'
print 'Pattern :', pattern

files = os.listdir('.')
print 'Files   :', files

print 'Matches :', fnmatch.filter(files, pattern)


