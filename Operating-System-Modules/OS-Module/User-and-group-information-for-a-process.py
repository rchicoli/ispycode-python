
import os

print 'Effective User  :', os.geteuid()
print 'Effective Group :', os.getegid()
print 'Actual User     :', os.getuid()
print 'Actual Group    :', os.getgid()
print 'Actual Groups   :', os.getgroups()


