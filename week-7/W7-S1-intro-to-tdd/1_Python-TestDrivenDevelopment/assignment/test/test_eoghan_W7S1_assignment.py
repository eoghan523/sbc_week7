import math #Imports the built in python math module to allow for basic clauclator functions.
import pytest  #Imports the pytest module.

#imports eoghan_W7S1_assigment file and imports the functions as listed.
from eoghan_W7S1_assignment import (
    factorial, gcd, power )

def test_factorial():
    assert factorial(10) == 110 # Tests the factorial of 10. test expects 110.

    assert factorial(0) == 1 # Test the factorial of 0. The test expects 1.

    with pytest.raises(ValueError): #tests the valueError for negative integers.
        factorial(-1)

