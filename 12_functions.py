
"""
Task 1: Greeting
Write a function that takes a name as an argument and prints a greeting message like "Hello, [name]!".
"""
def greet(name):
    # Prints a greeting message with the provided name.
    print(f"Hello, {name}!")


"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square(num):
    # Returns the square of the provided number.
    return num ** 2


"""
Task 3: Even or Odd
Write a function that takes a number as an argument that 
returns `True` if the number is even, and `False` otherwise.
"""
def is_even(num):
    # Returns True if the number is even, otherwise False.
    return num % 2 == 0


"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def rectangle_area(length, width):
    # this alculates and returns the area of a rectangle using the formula: length * width.
    return length * width


"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula.
"""
def celsius_to_fahrenheit(celsius):
    # Converts Celsius to Fahrenheit using the formula: (Celsius * 9/5) + 32.
    return (celsius * 9/5) + 32


"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
def average(numbers):
    # Calculates the mean by summing the list and dividing by its length. if the list is empty, return 0.
    return sum(numbers) / len(numbers) if numbers else 0


"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted total if provided.
"""
def total_calculator(price, quantity, discount=0.0):
    # ,ultiplies price and quantity to get the total.
    total = price * quantity
    # If a discount is provided, subtract the discounted amount from the total.
    if discount:
        total -= total * discount
    return total
