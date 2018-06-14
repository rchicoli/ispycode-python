
import fileinput
import re
import sys

pattern = re.compile(sys.argv[1])

for line in fileinput.input(sys.argv[2:]):
  if pattern.search(line):
    fmt = '{filename}:{lineno:<2}:{line}'
    print fmt.format(filename=fileinput.filename(),
                     lineno=fileinput.filelineno(),
                     line=line.rstrip())


