
from shutil import make_archive

f = make_archive('myarchive', 'gztar', 'dir1')
print(f)


