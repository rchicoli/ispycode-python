
import os
import pwd

name = pwd.getpwuid( os.getuid() )[ 0 ]
print name


