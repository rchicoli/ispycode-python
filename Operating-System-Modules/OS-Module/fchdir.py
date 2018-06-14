
import os

print( os.getcwd() )

fd  = os.open( "/tmp", os.O_RDONLY )
os.fchdir(fd)

print( os.getcwd() )


