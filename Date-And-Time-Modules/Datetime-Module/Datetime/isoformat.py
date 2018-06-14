
from datetime import datetime

dt = datetime.today()

str = dt.isoformat()
print(str)

str = dt.isoformat('_')
print(str)


