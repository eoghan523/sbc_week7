import math #Imports the built in python math module to allow for basic clauclator functions.
import pytest  #Imports the pytest module.

#imports eoghan_W7S1_assigment file and imports the functions as listed.
from eoghan_W7S1_assignment import (
    factorial, gcd, power, is_sorted, fibonacci, )

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

def is_sorted(lst):
    # Check if the list is equal to its sorted version
    return lst == sorted(lst)

def fibonacci(n):
    # Check if the input is a negative integer
    if n < 0:
        # Raise a ValueError if the input is negative
        raise ValueError("Input must be a non-negative integer")
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Iterate n times to compute the nth Fibonacci number
    for _ in range(n):
        # Update a to be the next Fibonacci number and b to the sum of a and b
        a, b = b, a + b
    
    # Return the nth Fibonacci number
    return a
