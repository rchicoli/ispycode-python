
import shutil

def myzip():
  pass

shutil.register_archive_format('myzip', myzip, description='myzip file' )

for name, description in shutil.get_archive_formats():
  print('%-5s: %s' % (name,description))


