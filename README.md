# OFFICIAL AUTO-GRADER FOR PROGRAMMING ASSIGNMENTS - SOKA UNIVERSITY OF AMERICA

Creator: Ngoc Doan

Description: The auto-grader program is to automatically grade students' programming submissions for the Introduction to Computer Science class at Soka University of America when they submit on Gradescope.

## My approach to design the auto-grader

As I have to design an auto-grader for each assignment and each week's assignments follow different concepts, I have developed a general structure for one auto-grader to save time.

Every autograder has the following files:
```bash
├── requirements.txt
├── run_autograder
├── run_tests.py
├── setup.sh
├── solution
│   └── hw[number].py
├── tests
│   ├── __init__.py
│   └── test_hw.py
```

The first four files are mandatory in order for the program to run on Gradescope. The `solution` folder contains my solution to the assignment. The `tests` folder is my unit tests. I seperate them so that I can recognize whether the bugs come from my solution or the test cases I design.

In the `test.hw.py` file, which is the main test file, mostly I will set up two `setUp()` functions to open my solution and students' submission and mock the user input. Then I set up a `test_hw()` for all test cases as students can only receive the grade if they pass all test cases. 

```
class TestHW(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def setUpAns(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect = mock_input):
            solution.main()
        return mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable = StringIO)
    def setUpSub(self, mock_input, mock_stdout):
        with patch('builtins.input', side_effect = mock_input):
            hw3.main()
        return mock_stdout.getvalue()
        
    @weight(9)
    def test_hw(self):
        ...
```

## Some assignments that quite challenged me 

#### homework 3 + 4 (Week 2)
The first few weeks students only know to print the results instead of returning them. As I tried to compare two print statements (my solution and student's submission), this proves to be not the best way. For example, if an assignment asks students to calculate something and print the result with 2 decimal places, I would use the traditional f string to format the result, while students may use other easier functions (like `round()`), which ouputs the result that may not be consistent with the f string. Thus I have learned to modify the autograders to split the print statements and convert the results into the original type to compare.
#### homework 9 (Week 4)
For this auto-grader, I create a function to completely generate the test cases.
#### homework 11 (Week 4)
This homework deals with file handling, which takes the content in a txt file as an input and then write the output in another file. Thus it was challenging for me to make sure that the input and output are properly tested.
#### homework 16 (Week 6)
Students learn about defining functions during this week. And this homework is to create a program to convert a decimal number into a number of another base by creating four functions and using the while loop to prompt user to enter the suitable decimal number and base. Thus I have two sets of tests for each function - the first set is unsuitable inputs to test the while loop and the second set is suitable inputs to pass the while loop.

## Future implementations
- [ ] Create a document for students to understand the error messages and debug better
- [ ] Design a program to generate auto-graders
- [ ] Explore the Gradescope decorators
- [ ] Test the autograders locally using Docker