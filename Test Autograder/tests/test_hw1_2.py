import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight
import solution.hw1_2_solution as solution
try:
    from hw1_2 import *
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function or not change the original file name.')


class TestHw1_2(unittest.TestCase):
    def setUp(self):
        with patch('sys.stdout', new = StringIO()) as list_ans:
            solution.main()
            self.list_ans = str(list_ans.getvalue()).split('\n')
        with patch('sys.stdout', new = StringIO()) as list_submission:
            main()
            self.list_submission = str(list_submission.getvalue()).split('\n')
        self.i = 0
    
    @weight(1)
    def test_hw1_2a(self):
        self.assertEqual(self.list_ans[self.i], self.list_submission[self.i])
        self.i += 1

    @weight(1)
    def test_hw1_2b(self):
        self.assertEqual(self.list_ans[self.i], self.list_submission[self.i])
        self.i += 1
    
    @weight(1)
    def test_hw1_2c(self):
        self.assertEqual(self.list_ans[self.i], self.list_submission[self.i])
        self.i += 1
    
    @weight(1)
    def test_hw1_2d(self):
        self.assertEqual(self.list_ans[self.i], self.list_submission[self.i])
        self.i += 1
    
    @weight(1)
    def test_hw1_2e(self):
        self.assertEqual(self.list_ans[self.i], self.list_submission[self.i])
        self.i += 1
    
    @weight(1)
    def test_hw1_2f(self):
        self.assertEqual(self.list_ans[self.i], self.list_submission[self.i])
        self.i += 1
    
