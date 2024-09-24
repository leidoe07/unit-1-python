"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
my_number = 1
while my_number<=10:
    print(my_number)
    my_number += 1



"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
my_number = 10
while my_number>=1:
    print(my_number)
    my_number -= 1
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
my_number = int(input('input a number'))
while my_number<=1000:
    print(my_number)
    my_number *= 10
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
correct_password = str('leidoe07')
user_input = " "
while correct_password != user_input:
    user_input = input('Enter a password')
    correct_password == user_input:   
    break
    print('Correct')
    
"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""