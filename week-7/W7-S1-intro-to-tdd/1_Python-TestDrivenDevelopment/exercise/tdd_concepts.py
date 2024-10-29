# tdd_concepts.py

import unittest

# Step 1: Palindrome Check. Checks if a given string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Step 2: Alphabet Check. Checks if a given string contains only alphabetic characters.
def is_alpha(s):
    return s.isalpha()

# Step 3: Basic Math Operations. Returns the sum of two numbers.
def add(a, b):
    return a + b


# Step 4: Fibonacci Sequence. Returns the nth Fibonacci number
def fibonacci(n):
  
    if n < 0:
        raise ValueError("Input cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Step 4: Anagram Check
def is_anagram(s1, s2):
    """Checks if two strings are anagrams of each other."""
    return sorted(s1) == sorted(s2)

# Unit tests
class TestTDDConcepts(unittest.TestCase):
    # Tests for is_palindrome
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))

    # Tests for is_alpha
    def test_is_alpha(self):
        self.assertTrue(is_alpha("hello"))
        self.assertFalse(is_alpha("hello123"))

    # Tests for add and multiply
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)

    # Tests for fibonacci
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    # Tests for is_anagram
    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertFalse(is_anagram("hello", "world"))
        self.assertTrue(is_anagram("a", "a"))
        self.assertFalse(is_anagram("a", "b"))

if __name__ == '__main__':
    unittest.main()
