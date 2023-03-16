import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw12 as hw12
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw12 as solution
import random

class TestHW(unittest.TestCase):
    @weight(9)
    def test_hw(self):
        s = ["01/31/1000", "00/11/1111", "12/-1/2033", "11/11/0001", "12/01/35647"]
        for i in s:
            ans = solution.check_date(i)
            submission = hw12.check_date(i)
            self.assertEqual(ans, submission, "Failed with s = " + i)
    
