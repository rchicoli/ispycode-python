
import os

FILES = (
    os.curdir,
    "/",
    "example.py",
    "/etc/resolv.conf",
    "/home/dennis/no_file"
    )

for file in FILES:
    print '{:17}'.format(file), ":",
    if os.path.exists(file):
        print "EXISTS",
    if os.path.isabs(file):
        print "ISABS",
    if os.path.isdir(file):
        print "ISDIR",
    if os.path.isfile(file):
        print "ISFILE",
    if os.path.islink(file):
        print "ISLINK",
    if os.path.ismount(file):
        print "ISMOUNT",
    print


