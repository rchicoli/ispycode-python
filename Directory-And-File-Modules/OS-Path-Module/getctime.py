
import os.path
from datetime import datetime

t = os.path.getctime('example.py')

print(datetime.fromtimestamp(t))


