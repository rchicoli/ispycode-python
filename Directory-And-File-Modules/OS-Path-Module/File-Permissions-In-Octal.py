
import os , stat

perms = stat.S_IMODE(os.stat('example.py').st_mode)
print oct(perms)


