import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw14 as hw14
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw14 as solution
import random

class TestHW(unittest.TestCase):
    @weight(9)
    def test_hw(self):
        s = ["01/31/1000", "00/11/1111", "12/-1/2033", "11/11/0001", "12/31/1000", "02/31/2000", "13/31/3654", "09/31/2455", "02/28/69890", "02/29/0040", "02/29/0100", "02/29/0400", "02/29/0240", "02/29/0200", "02/29/0600", "02/29/0800", "02/29/1100", "02/29/1000", "02/29/1400", "02/29/1140", "02/29/1598", "02/29/2023", "02/29/2024"]
        for i in s:
            ans = solution.check_date(i)
            submission = hw14.check_date(i)
            self.assertEqual(ans, submission, "Failed with s = " + i)
    
