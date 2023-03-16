import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight
try:
    import hw1 as hw1
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw1 as solution

class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect = mock_input):
            hw1.main()
        return mock_stdout.getvalue()
    
    @weight(9)    
    def test_hw(self):
        message = ["Hello, World!", "abc", "", "66075", ""]
        n = [3, 21, 0, 0, 4]
        for i in range(len(n)):
            ans = self.setUpAns([message[i], n[i]])
            submission = self.setUpSub([message[i], n[i]])
            self.assertEqual(ans, submission, "Failed at n = " + str(n[i]) + " and message = " + str(message[i]))
    
