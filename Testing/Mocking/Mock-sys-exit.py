
import sys
from mock import patch

def function():
  print("in function")
  sys.exit(1)

def test_function():
  with patch('sys.exit') as exit_mock:
    function()
    assert exit_mock.called


