import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw16 as hw16
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw16 as solution
import random

class TestHW(unittest.TestCase):

    def getNumTest(self):
        #wrong cases
        getNumTests = ["abc", "", "abc123", "123abc", "-1", "1.6", "1234,abc", "1234,23,234", "1234,123,123", "0"]
        with patch('builtins.input', side_effect=getNumTests):
            ans = solution.getNum()
        with patch('builtins.input', side_effect=getNumTests):
            submission = hw16.getNum()
        self.assertEqual(ans, submission, "getNum() failed")

        #right case
        with patch('builtins.input', side_effect="12,123,345"):
            ans = solution.getNum()
        with patch('builtins.input', side_effect="12,123,345"):
            submission = hw16.getNum()
        self.assertEqual(ans, submission, "getNum() failed")
        
    def getBaseTest(self):
        #wrong cases
        getBaseTests = ["abc", "", "abc123", "123abc", "-1", "1.6", "1234,abc", "1234,23,234", "1234,123,123", "0", "35"]
        with patch('builtins.input', side_effect=getBaseTests):
            ans = solution.getBase()
        with patch('builtins.input', side_effect=getBaseTests):
            submission = hw16.getBase()
        self.assertEqual(ans, submission, "getBase() failed")
        
        #right case
        with patch('builtins.input', side_effect="2"):
            ans = solution.getBase()
        with patch('builtins.input', side_effect="2"):
            submission = hw16.getBase()
        self.assertEqual(ans, submission, "getBase() failed")
        
    def convertTest(self):
        for i in range(50):
            num = random.randint(1, 100000)
            base = random.randint(2, 35)
            ans = solution.convert(num,base)
            submission = hw16.convert(num,base)
            self.assertEqual(ans, submission, "convert() failed with num = " + str(num) + " and base = " + str(base))

    def mainTest(self):
        #check if the while works:
        tests = ["abc", "", "abc123", "123abc", "-1", "1.6", "1234,abc", "1234,23,234", "1234,123,123", "1234", "0", "37", "16"]
        with patch('builtins.input', side_effect=tests):
            ans = solution.main()
        with patch('builtins.input', side_effect=tests):
            submission = hw16.main()
        self.assertEqual(ans, submission, "main() failed")
        
        for i in range(20):
            num = random.randint(1, 100000)
            base = random.randint(2, 35)
            with patch('builtins.input', side_effect=[str(num), str(base)]):
                ans = solution.main()
            with patch('builtins.input', side_effect=[str(num), str(base)]):
                submission = hw16.main()
            self.assertEqual(ans, submission, "main() failed at num " + str(num) + " base = " + str(base))
                
    
    @weight(9)
    def test_hw(self):
        self.getNumTest()
        self.getBaseTest()
        self.convertTest()
        self.mainTest()
        
     
