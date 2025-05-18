# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# - Smallest Unit Of Testing
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suite
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# - A Full Report Contains The Failure Or Succeed
# -------------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html
# -----------------------------------------------

import unittest # Import the unittest module

assert 3 * 8 == 24, "Should Be 24" # This is an assertion statement
# that checks if 3 * 8 equals 24 and prints "Should Be 24" if
#  it does not equal 24

def test_case_one(): # Define a test case function

  assert 5 * 10 == 50, "Should Be 50" # This is an assertion statement
# that checks if 5 * 10 equals 50 and prints "Should Be 50" if 
#  it does not equal 50

def test_case_two(): # Define another test case function

  assert 5 * 50 == 250, "Should Be 250"

if __name__ == "__main__": # This block will only run if the script
  # is executed directly instead of being imported

  test_case_one()   # Call the test_case_one function
  test_case_two() # Call the test_case_two function

  print("All Tests Passed") # Print a message indicating that
  # all tests passed and if one of the tests failed, it will not
  #  print this message

class MyTestCase(unittest.TestCase): # Define a test case class that 
  #inherits from unittest.TestCase

  def test_one(self): # Define a test method
    # This method will be run as a test case

    self.assertTrue(100 > 99, "Should Be True") # This is an assertion
    # statement that checks if 100 is greater than 99 and prints
    # "Should Be True" if it is not

  def test_two(self): # Define another test method

    self.assertEqual(40 + 60, 100, "Should Be 100") # This is an
    # assertion statement that checks if 40 + 60 equals 100 and
    # prints "Should Be 100" if it does not

  def test_three(self):

    self.assertGreater(102, 101, "Should Be True") # This is an assertion
    # statement that checks if 100 is greater than 101 and prints
    # "Should Be True" if it is not

if __name__ == "__main__": # This block will only run if the script
  # is executed directly

  unittest.main() # This line runs the test case class and
  #prints the results of the tests