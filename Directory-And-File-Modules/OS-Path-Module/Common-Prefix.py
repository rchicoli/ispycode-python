
import os

def commonprefix(args, sep='/'):
        return os.path.commonprefix(args).rpartition(sep)[0]

dirs = ('/etc/default/rsync','/etc/default/rsyslog','/etc/default/rcS')

dir = commonprefix(dirs)
print(dir)


