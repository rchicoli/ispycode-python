
import filecmp

# Construct a new directory comparison object
dc = filecmp.dircmp('/tmp/dir1','/tmp/dir2')

# Print (to sys.stdout) comparison
dc.report()


