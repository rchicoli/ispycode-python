
import os.path

stat1  = os.stat('example.py')
stat2  = os.stat('example.py')
stat3  = os.stat('file.txt')

print(os.path.samestat(stat1,stat2))
print(os.path.samestat(stat1,stat3))


