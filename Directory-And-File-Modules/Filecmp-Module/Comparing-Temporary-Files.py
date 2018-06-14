
import filecmp
from tempfile import NamedTemporaryFile

f1 = NamedTemporaryFile(delete=False)
f1.write("Hello World")
f1.close()

f2 = NamedTemporaryFile(delete=False)
f2.write("Hello World")
f2.close()

print(f1.name)
print(f2.name)
results = filecmp.cmp(f1.name,f2.name)
print(results)


