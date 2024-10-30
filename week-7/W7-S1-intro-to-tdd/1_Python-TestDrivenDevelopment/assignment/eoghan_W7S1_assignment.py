import math #Imports the inbuilt python math module
import pytest #Imports pytest module for use.

#**Factorial Calculation**

def factorial(n):
    if n < 0:       #Checks if the input is a negaative integer
        raise ValueError("can't be a negative integer.")  #Raises a value error and message
    result = 1     #Initiates the result to 1.
    
      # Iterate from 2 to n (inclusive) to calculate the factorial
    for i in range(2, n + 1):
     # Multiply the current result by the current integer i
        result *= i
        
     # Return the factorial 
    return result

#**GCD Calculation**  A function to clculate gcd (greatest common divisor).
def gcd(a, b):
    # Continue looping as long as b is not zero
    while b:
        # a is assigned the value of b, and b is assigned the value of a % b. This updates the values to continue the algorithm.
        a, b = b, a % b
    
    # When b becomes zero, the function returns a, which is the GCD of the original inputs.
    return a


#**Power Calculation** 
def power(base, exponent):
 # Return the result of base raised to the power of exponent
    return base ** exponent