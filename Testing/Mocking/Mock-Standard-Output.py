
import unittest
from StringIO import StringIO
from mock import patch

def hello():
   print('Hello World')

class MyTest(unittest.TestCase):

   @patch('sys.stdout', new_callable=StringIO)
   def test(self,mock_stdout):
      hello()
      output = mock_stdout.getvalue()
      assert "Hello World" in output


