import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw5 as hw5
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw5 as solution
import random

class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            hw5.main()
        return mock_stdout.getvalue()
    
 #   @visibility("hidden")
    @weight(9)    
    def test_hw(self):
        for i in range(50):
            dollar = round(random.uniform(0,10000), 2)
            ans = self.setUpAns(dollar)
            submission = self.setUpSub(dollar)
            self.assertEqual(ans, submission, "Failed with dollar value = " + str(dollar))
    
