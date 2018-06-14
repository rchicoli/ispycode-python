
import itertools
for item in itertools.zip_longest('ABCD', 'xy', fillvalue='-'):
    print (item)


