import math #Imports the built in python math module to allow for basic clauclator functions.
import pytest  #Imports the pytest module.

#imports eoghan_W7S1_assigment file and imports the functions as listed.
from eoghan_W7S1_assignment import(factorial, gcd, power, is_sorted, fibonacci, matrix_addition)


def test_factorial():
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
