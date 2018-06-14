
import os.path

results = os.path.lexists('/home/dennis/examples/example.py')
print(results)

results = os.path.lexists('/tmp/file1.txt')
print(results)

results = os.path.lexists('/tmp/nofile')
print(results)


