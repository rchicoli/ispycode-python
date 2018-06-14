
import filecmp

file1 = '/tmp/file1.txt'
file2 = '/tmp/file2.txt'
file3 = '/tmp/file3.txt'
file4 = '/tmp/file4.txt'

test1 = filecmp.cmp(file1,file2)
test2 = filecmp.cmp(file1,file3)
test3 = filecmp.cmp(file1,file4)

results = test1 & test2 & test3
print(results)


