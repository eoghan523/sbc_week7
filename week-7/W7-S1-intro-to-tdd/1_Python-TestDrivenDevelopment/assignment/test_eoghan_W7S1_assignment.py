import math #Imports the built in python math module to allow for basic clauclator functions.
import pytest  #Imports the pytest module.

#imports eoghan_W7S1_assigment file and imports the functions as listed.
from eoghan_W7S1_assignment import (
    factorial, gcd, power, is_sorted, fibonacci,
    matrix_addition, area_rectangle, area_circle, is_perfect_square
)


def test_factorial():
    assert factorial(5) == 120 #tests the factorial of 5. The test expects 120
    assert factorial(10) == 3628800 # Tests the factorial of 10. test expects 3628800.
    assert factorial(0) == 1 # Test the factorial of 0. The test expects 1.

    with pytest.raises(ValueError): #tests the valueError for negative integers.
        factorial(-1)

# Define a test function for GCD (Greatest Common Divisor).
def test_gcd():
    # Test GCD of 6 and 16 (expected: 2).
    assert gcd(6, 16) == 2
    # Test GCD of 101 and 10 (expected: 1).
    assert gcd(101, 10) == 1
    # Test GCD of 0 and 5 (expected: 5).
    assert gcd(0, 5) == 5
    # Test GCD of 5 and 0 (expected: 5).
    assert gcd(5, 0) == 5

# Define a test function for power calculation.
def test_power():
    # Test 2 raised to the power of 3 (expected: 8).
    assert power(2, 3) == 8
    # Test 5 raised to the power of 0 (expected: 1).
    assert power(5, 0) == 1
    # Test 3 raised to the power of 3 (expected: 27).
    assert power(3, 3) == 27

def test_is_sorted():
    assert is_sorted([1, 2, 3, 4]) is True  # Tests a sorted list.
    assert is_sorted([4, 3, 2, 1]) is False  # Tests an unsorted list.


def test_fibonacci():
    assert fibonacci(0) == 0  # Tests the 0th Fibonacci number.
    assert fibonacci(1) == 1  # Tests the 1st Fibonacci number.
    assert fibonacci(5) == 5  # Tests the 5th Fibonacci number.
    assert fibonacci(10) == 55  # Tests the 10th Fibonacci number.

    with pytest.raises(ValueError):  # Tests that ValueError is raised for negative inputs.
        fibonacci(-1)


# Test for matrix_addition function
def test_matrix_addition():
    # Define two matrices to add
    matrix1 = [[1, 2], [3, 4]]      # First matrix to be tested
    matrix2 = [[5, 6], [7, 8]]      # Second matrix to be tested
    # Test addition of matrix1 and matrix2. The expected output is [[6, 8], [10, 12]]
    assert matrix_addition(matrix1, matrix2) == [[6, 8], [10, 12]]
    # Test for ValueError if matrices are of different dimensions
    with pytest.raises(ValueError):      #tests the ValueError function
        matrix_addition([[1, 2], [3, 4]], [[5, 6]])

# Area of Rectangle Tests
def test_area_rectangle():  # Define a test function for the area of a rectangle
    # Test with a length of 5 and width of 10, expecting an area of 50
    assert area_rectangle(5, 10) == 50  # Verify that the area of 5 * 10 is 50
    # Test with a length of 0 and width of 10, expecting an area of 0
    assert area_rectangle(0, 10) == 0  # Verify that the area of 0 * 10 is 0

# Area of Circle Tests
def test_area_circle():  # Define a test function for the area of a circle
    # Test with a radius of 1, expecting the area to be close to pi (π)
    # Using pytest.approx to allow for minor floating-point variations
    assert area_circle(1) == pytest.approx(math.pi, 0.01)  # Check that the area is approximately π
    # Test with a radius of 0, expecting an area of 0
    assert area_circle(0) == 0  # Verify that the area of a circle with radius 0 is 0

# Perfect Square Check Tests
def test_is_perfect_square():  # Define a test function for checking perfect squares
    # Test with 16, which is a perfect square (4 * 4), expecting True
    assert is_perfect_square(16) is True  # Check that 16 is identified as a perfect square
    # Test with 20, which is not a perfect square, expecting False
    assert is_perfect_square(20) is False  # Check that 20 is identified as not a perfect square
    # Test with 0, which is a perfect square (0 * 0), expecting True
    assert is_perfect_square(0) is True  # Verify that 0 is identified as a perfect square





### 5. **📤 Print and verify results**  

#PS C:\Users\eogha\sbc_week7\week-7\W7-S1-intro-to-tdd\1_Python-TestDrivenDevelopment\assignment> pytest -v
#============================================================== test session starts ===============================================================
#platform win32 -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\eogha\AppData\Local\Programs\Python\Python312\python.exe
#cachedir: .pytest_cache
#rootdir: C:\Users\eogha\sbc_week7\week-7\W7-S1-intro-to-tdd\1_Python-TestDrivenDevelopment\assignment
#collected 9 items                                                                                                                                  

#test_eoghan_W7S1_assignment.py::test_factorial PASSED                                                                                       [ 11%]
#test_eoghan_W7S1_assignment.py::test_gcd PASSED                                                                                             [ 22%] 
#test_eoghan_W7S1_assignment.py::test_power PASSED                                                                                           [ 33%] 
#test_eoghan_W7S1_assignment.py::test_is_sorted PASSED                                                                                       [ 44%] 
#test_eoghan_W7S1_assignment.py::test_fibonacci PASSED                                                                                       [ 55%] 
#test_eoghan_W7S1_assignment.py::test_matrix_addition PASSED                                                                                 [ 66%] 
#test_eoghan_W7S1_assignment.py::test_area_rectangle PASSED                                                                                  [ 77%] 
#test_eoghan_W7S1_assignment.py::test_area_circle PASSED                                                                                     [ 88%]
#test_eoghan_W7S1_assignment.py::test_is_perfect_square PASSED                                                                               [100%] 

#=============================================================== 9 passed in 0.02s ================================================================ 
#PS C:\Users\eogha\sbc_week7\week-7\W7-S1-intro-to-tdd\1_Python-TestDrivenDevelopment\assignment> 

