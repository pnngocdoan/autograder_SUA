import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw11 as hw11
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw11 as solution
import random

class TestHW(unittest.TestCase):
    def setUpAns(self):
        solution.main()
        ansFile = open("[Solution]StudentSubmissions.txt", "r")
        ansData = ansFile.readlines()
        return ansData
    
    def setUpSub(self):
        hw11.main()
        subFile = open("StudentSubmissions.txt", "r")
        subData = subFile.readlines()
        return subData
    
 #   @visibility("hidden")
    @weight(9)    
    def test_hw(self):
        ans = self.setUpAns()
        submission = self.setUpSub()
        self.assertEqual(ans, submission)
    
