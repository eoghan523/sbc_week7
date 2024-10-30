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
