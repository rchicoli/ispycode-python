
import shutil

for name, description in shutil.get_archive_formats():
  print('%-5s: %s' % (name,description))


