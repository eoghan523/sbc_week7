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

def is_sorted(lst):
    # Check if the list is equal to its sorted version
    return lst == sorted(lst)


#**Fibonacci** Function to calculate the nth fibonacci number. 
def fibonacci(n):
    # Check if the input is a negative integer
    if n < 0:
        # Raise a ValueError if the input is negative
        raise ValueError("Input must be a non-negative integer")
    
    # This line Initializes the first two Fibonacci numbers
    a, b = 0, 1
    
    # Iterate n times to compute the nth Fibonacci number
    for _ in range(n):
        # Update a to be the next Fibonacci number and b to the sum of a and b
        a, b = b, a + b
    
    # Return the nth Fibonacci number
    return a

#**Matrix Addition** Function for adding two Matrices.
def matrix_addition(matrix1, matrix2):
    # Check if dimensions of both matrices match
    # First, check if the number of rows in both matrices are equal
    # Then, check if each pair of corresponding rows has the same length
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        # If the matrices do not have the same dimensions, raise a ValueError
        raise ValueError("Matrics must have the same dimensions...")
    
    # Add corresponding elements in the matrices
    result = [
        # For each row index `i` in `matrix1`, create a new row
        [
            # Add elements at the same column `j` in both `matrix1` and `matrix2`
            matrix1[i][j] + matrix2[i][j]
            for j in range(len(matrix1[0]))  # Iterates over each column in the row
        ]
        for i in range(len(matrix1))  # Iterates over each row
    ]
    
    # Return the resulting matrix containing the element-wise sums
    return result

#**Area of Rectangle** Function to calculate the Area of a Rectangle.
def area_rectangle(length, width):
    # Return area calculated as length multiplied by width
    return length * width

#**Area of Circle** Function to calculate the Area of a Circle.
def area_circle(radius):
    # Return area using formula π * r^2
    return math.pi * radius ** 2

#**Perfect Square Check** Function to calculate the Perfect Square.
def is_perfect_square(n):
    # Check if the input number is negative (negative numbers cannot be perfect squares)
    if n < 0:
        return False  # Return False immediately if n is negative

    # Calculate the integer square root of n by first finding the square root (returns a float)
    # and then converting it to an integer using int()
    root = int(math.sqrt(n))

    # Check if squaring the integer root gives back the original number n
    # If root * root equals n, then n is a perfect square; otherwise, it is not
    return root * root == n