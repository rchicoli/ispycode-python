
import fnmatch
import os

for file in os.listdir('.'):
  if fnmatch.fnmatchcase(file, '*.txt'):
    print file


