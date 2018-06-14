
import os.path
from datetime import datetime

t = os.path.getmtime('example.py')

print(datetime.fromtimestamp(t))


