import unittest
from unittest.mock import patch
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, visibility
try:
    import hw9 as hw9
except Exception:
    raise Exception(f'Could not process your file, remember to code under the main() function, not call the main() function, and set the file name correctly.')
import solution.hw9 as solution
import random
import string

class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', return_value = mock_input):
            hw9.main()
        return mock_stdout.getvalue()
    
    def random_string(self, length):
        word_source = string.ascii_lowercase
        sentence_length = 0
        sentence_source = []
        while sentence_length < length: 
            word_length = random.randint(1, length) % 10
            sentence_length += word_length
            word = []
            for i in range(word_length):
                word.append(random.choice(word_source))
            sentence_source.append(''.join(word))
        return ' '.join(sentence_source)
 
 #   @visibility("hidden")

    maxDiff = None
    
    @weight(9)
    def test_hw(self):
        
        for i in range(50):
            length = random.randint(1, 10000)
            string = self.random_string(length)
            ans = self.setUpAns(string).strip()
            submission = self.setUpSub(string).strip()
            self.assertEqual(ans, submission, "Failed with string length = " + str(length) + " and string = " + string)
    
