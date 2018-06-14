
import filecmp

equal = filecmp.cmp('/tmp/file1.txt','/tmp/file2.txt')
print(equal)

equal = filecmp.cmp('/tmp/file1.txt','/tmp/file3.txt')
print(equal)


