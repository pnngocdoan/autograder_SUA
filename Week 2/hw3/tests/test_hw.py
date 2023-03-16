import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw3 as hw3
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw3 as solution
import random

class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect = mock_input):
            hw3.main()
        return mock_stdout.getvalue()
        
 #   @visibility("hidden")
    @weight(9)
    def test_hw(self):
        n = [5, 10, 50, 100, 500, 1000, 5000, 100000]
        for i in range(len(n)):
            rand_list = []
            rand_list.append(n[i])
            for j in range(n[i]):
                rand_list.append(random.uniform(-10000,10000))
            ans = self.setUpAns(rand_list)
            submission = self.setUpSub(rand_list)
            self.assertEqual(ans, submission, "Failed with n = " + str(n[i]))
    
