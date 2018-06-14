
import os.path

def function(a, dir, files):
   print dir,": %d files"%len(files)

os.path.walk('/etc/apt', function, None)


