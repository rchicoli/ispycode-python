
import filecmp

myfiles = ['file1.txt','file2.txt','file3.txt']
match, mismatch, error = filecmp.cmpfiles('/tmp/dir1','/tmp/dir2',myfiles)

print "Matching: ", match
print "Mismatched: ", mismatch
print "Errors: ", error


