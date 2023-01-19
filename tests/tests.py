import unittest
from gradescope_utils.autograder_utils.decorators import weight

try:
    from hw1 import *
except Exception:
    raise Exception(f'Could not process your file, remember to work off of the template.')

class TestHw1(unittest.TestCase):
    def setUp(self):
        pass
    
    @weight(2)
    def test_hw1_1(self):
        ans = "Hello, World!"
        output = hw1_1()
        self.assertEqual(output, ans)
    
    @weight(1)
    def test_hw1_2a(self):
        ans = 1+10
        output = hw1_2a()
        self.assertEqual(output, ans)
        
    @weight(1)
    def test_hw1_2b(self):
        ans = 5-9
        output = hw1_2b()
        self.assertEqual(output, ans)
        
    @weight(1)
    def test_hw1_2c(self):
        ans = 2/3
        output = hw1_2c()
        self.assertEqual(output, ans)
        
    @weight(1)
    def test_hw1_2d(self):
        ans = 9//4
        output = hw1_2d()
        self.assertEqual(output, ans)
    
    @weight(1)
    def test_hw1_2e(self):
        ans = 7**5
        output = hw1_2e()
        self.assertEqual(output, ans)
    
    @weight(1)
    def test_hw1_2f(self):
        ans = 8*2
        output = hw1_2f()
        self.assertEqual(output, ans)
    
    @weight(3)
    def test_hw1_3(self):
        ans = "Hello, "
        output = hw1_3()[0:8]
        self.assertEqual(output, ans)
