
from tempfile import SpooledTemporaryFile

f = SpooledTemporaryFile(max_size=1024)
f.write("Hello")
f.seek(0)
print(f.readlines())
f.close()


