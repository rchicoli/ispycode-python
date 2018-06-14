
from tempfile import NamedTemporaryFile

f = NamedTemporaryFile(delete=False)
f.write("Hello World")
f.close()
print f.name


