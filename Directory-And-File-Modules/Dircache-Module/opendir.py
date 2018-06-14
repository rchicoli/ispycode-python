
import dircache

listing = dircache.opendir('/')

for f in listing:
    print f


