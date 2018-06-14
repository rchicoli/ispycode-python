
from tempfile import mkstemp
from os import close, write

handle, name = mkstemp()
write(handle, 'Hello World')
close( handle )

print(name)

f = open( name, 'r')
print(f.read())
f.close()


