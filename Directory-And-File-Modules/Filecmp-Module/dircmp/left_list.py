
import filecmp

dc = filecmp.dircmp('/tmp/dir1','/tmp/dir2')

print(dc.left_list)


