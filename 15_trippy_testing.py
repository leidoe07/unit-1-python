"""
Exercise 1: Divide
"""
def divide(a, b):
    """Divides two numbers, handling potential division by zero.

    Args:
      a: The numerator.
      b: The denominator.

    Returns:
      The quotient, or None if b is zero.
    """
    if b == 0:
        return None
    else:
        return a / b


assert divide(8, 0) is None  # Expected output: None (since division by zero is handled)
assert divide(8, 4) == 2  # Expected output: 2
# This tests if divide function handles division by zero and normal division properly.

"""
Exercise 2: Factorial
"""
def factorial(n):
    """Calculates the factorial of a non-negative integer.

    Args:
      n: A non-negative integer.

    Returns:
      The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


assert factorial(0) == 1  # The factorial of 0 is 1
assert factorial(8) == 40320  # The factorial of 8 is 40320
#  These assertions check for correct output of factorial function for edge case (0) and other integers.

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
    """Reverses a given string.

    Args:
      string: A string to be reversed.

    Returns:
      The reversed string.
    """
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


assert reverse_string("hello") == "olleh"  # The string "hello" should reverse to "olleh"
#  This test case checks if the reverse_string function correctly reverses the input string.

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
    """Generates the nth Fibonacci number.

    Args:
      n: The index of the Fibonacci number to calculate.

    Returns:
      The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(1) == 1  # The 1st Fibonacci number is 1
assert fibonacci(9) == 34  # The 9th Fibonacci number is 34
# These assertions make sure the Fibonacci sequence is calculated correctly at the 1st and 9th positions.

"""
Exercise 5: Email Validation
"""
import re

def is_valid_email(email):
    """Determines whether the email is valid or not.

    Args:
      email: The email to validate.

    Returns:
      Boolean value if the email is valid.
    """
    email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$"
    return re.match(email_regex, email) is not None


assert is_valid_email("leilanidore07@gmail.com")  # Should return True for a valid email
assert not is_valid_email("thissite.google.com")  # Should return False for an invalid email
# This tests for both valid and invalid email formats using regex pattern matching.
