
from datetime import datetime

text = '2012-09-20'
format = "%b %d %Y"

dt = datetime.strptime(text, '%Y-%m-%d')

print(dt)


