
import os
import os.path

for user in [ 'root', 'dennis', 'news' ]:
    lookup = '~' + user
    print lookup, ':', os.path.expanduser(lookup)


