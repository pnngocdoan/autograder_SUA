import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw15 as hw15
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw15 as solution
import random

class TestHW(unittest.TestCase):

    def getNumTest(self):
        getNumTests = ["abc", "", "abc123", "123abc", "-1", "1.6", "1,6", "0"]
        with patch('builtins.input', side_effect=getNumTests):
            ans = solution.getNum()
        with patch('builtins.input', side_effect=getNumTests):
            submission = hw15.getNum()
        self.assertEqual(ans, submission, "getNum() failed")
    def dec2hexTest(self):
        for i in range(30):
            test = random.randint(1, 10000)
            ans = solution.dec2hex(test)
            submission = hw15.dec2hex(test)
            self.assertEqual(ans, submission, "dec2hex() failed with num = " + str(test))


    def mainTest(self):
        #check if the while works:
        getNumTests = ["abc", "", "abc123", "123abc", "-1", "1.6", "1,6", "0"]
        with patch('builtins.input', side_effect=getNumTests):
            ans = solution.main()
        with patch('builtins.input', side_effect=getNumTests):
            submission = hw15.main()
        self.assertEqual(ans, submission, "main() failed")
        
        for i in range(15):
            test = random.randint(1, 10000)
            with patch('builtins.input', return_value=str(test)):
                ans = solution.main()
            with patch('builtins.input', return_value=str(test)):
                submission = hw15.main()
            self.assertEqual(ans, submission, "main() failed at num = " + str(test))
    
    @weight(9)
    def test_hw(self):
        self.getNumTest()
        self.dec2hexTest()
        self.mainTest()
        
     