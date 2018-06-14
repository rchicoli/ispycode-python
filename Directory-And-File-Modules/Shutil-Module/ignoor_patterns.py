
from shutil import copytree, ignore_patterns

copytree('dir1','dir2', ignore=ignore_patterns('*.py', '*.java'))


