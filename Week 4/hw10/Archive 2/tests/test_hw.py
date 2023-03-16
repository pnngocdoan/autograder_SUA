import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw10 as hw10
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw10 as solution
import random
import math

class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            hw10.main()
        return mock_stdout.getvalue()
    
    def setUpTestFile(self, number):
        file = open('test.txt', 'w')
        fileContent = []
        for i in range(number):
            fileContent.append(str(random.uniform(0.0001,10000)) + "\n")
        file.writelines(fileContent)
        file.close()
 #   @visibility("hidden")
    @weight(9)    
    def test_hw(self):
        n = [5, 10, 50, 100, 500, 1000, 5000, 100000]
        for i in range(len(n)):
            self.setUpTestFile(n[i])
            ans = self.setUpAns("test.txt")
            submission = self.setUpSub("test.txt")

            ans = float(ans.split('=')[-1].strip())
            submission = float(submission.split('=')[-1].strip())
            
            self.assertEqual(ans, submission)
    
