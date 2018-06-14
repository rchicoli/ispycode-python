
import shutil

print('--before--')
for name, description in shutil.get_archive_formats():
  print('%-5s: %s' % (name,description))

shutil.unregister_archive_format('bztar')

print('--after--')
for name, description in shutil.get_archive_formats():
  print('%-5s: %s' % (name,description))


