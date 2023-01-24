import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight
import solution.hw1_3_solution as solution
try:
    from hw1_3 import *
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function or not change the original file name.')

class TestHw1_3(unittest.TestCase):
    def setUp(self):
        pass
    @weight(3)
    def test_hw1_3(self):
        with patch('sys.stdout', new = StringIO()) as ans:
            solution.main()
            ans = str(ans.getvalue())
        with patch('sys.stdout', new = StringIO()) as submission:
            main()
            submission = str(submission.getvalue())
            self.assertEqual(ans[:7],submission[:7])
            self.assertEqual(ans[-1],submission[-1])
    