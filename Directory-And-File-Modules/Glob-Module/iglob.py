
import glob

iterator  = glob.iglob('*.txt')
for fname in iterator :
  print(fname)


