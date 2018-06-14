
import os

st = os.stat('example.py')
print 'st_mode :', st.st_mode
print 'st_ino  :', st.st_ino
print 'st_dev  :', st.st_dev
print 'st_nlink:', st.st_nlink
print 'st_uid  :', st.st_uid
print 'st_gid  :', st.st_gid
print 'st_size :', st.st_size
print 'st_atime:', st.st_atime
print 'st_mtime:', st.st_mtime
print 'st_ctime:', st.st_ctime


