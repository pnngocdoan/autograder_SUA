import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight
import hw1_2_solution as solution
try:
    from hw1_2 import *
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function or not change the original file name.')

class TestHw1_2(unittest.TestCase):
    def setUp(self):
        pass
    
    @weight(1)
    def test_single_output(self, ans, submission):
        self.assertEqual(ans, submission)
    
    
    def test_hw1_2(self):
        with patch('sys.stdout', new = StringIO()) as list_ans:
            solution.main().getvalue().split('\n')
        with patch('sys.stdout', new = StringIO()) as list_submission:
            main().getvalue().split('\n')
        for i in range(len(list_ans)):
            self.test_single_output(list_ans[i], list_submission[i])
    