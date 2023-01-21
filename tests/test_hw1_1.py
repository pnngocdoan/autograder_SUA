import unittest
from gradescope_utils.autograder_utils.decorators import weight
from unittest.mock import patch
from io import StringIO
try:
    from hw1_1 import *
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function or not change the original file name.')

class TestHw1_1(unittest.TestCase):
    def setUp(self):
        pass
    
    @weight(2)
    def test_hw1_1(self):
        ans = "Hello, World!\n"
        with patch('sys.stdout', new = StringIO()) as submission:
            main()
            self.assertEqual(submission.getvalue(), ans)
