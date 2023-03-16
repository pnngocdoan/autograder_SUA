import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight
try:
    import hw2 as hw2
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw2 as solution

class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            hw2.main()
        return mock_stdout.getvalue()
    
    @weight(9)
    def test_hw(self):
        m = [2.336, 0, -9.78689, 13469.879231, 10]
        for i in range(len(m)):
            ans = self.setUpAns(m[i])
            submission = self.setUpSub(m[i])
            self.assertEqual(ans, submission, "Failed at m = " + str(m[i]))
            
