
import filecmp

dc = filecmp.dircmp('/tmp/dir1','/tmp/dir2')
dc.report_full_closure()


