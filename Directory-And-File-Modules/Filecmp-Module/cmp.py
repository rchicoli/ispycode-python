
import filecmp

val = filecmp.cmp('/tmp/file1.txt','/tmp/file2.txt')
print(val)

val = filecmp.cmp('/tmp/file1.txt','/tmp/file3.txt')
print(val)


