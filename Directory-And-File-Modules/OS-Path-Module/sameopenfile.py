
import os.path

fd1  = os.open( 'example.py', os.O_RDONLY )
fd2  = os.open( 'example.py', os.O_RDONLY )
fd3  = os.open( 'file.txt', os.O_RDONLY )

print(os.path.sameopenfile(fd1,fd2))
print(os.path.sameopenfile(fd1,fd3))


