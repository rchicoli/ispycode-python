
import fnmatch
import os
import re

pattern = fnmatch.translate("*.txt")

for file in os.listdir('.'):
  if re.match(pattern, file):
    print file

print "(pattern was %s)" % pattern


