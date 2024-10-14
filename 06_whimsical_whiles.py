"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
my_number = 1
while my_number <= 10:
    print(my_number)
    my_number += 1  # Increment the counter


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
my_number = 10
while my_number >= 1:
    print(my_number)
    my_number -= 1  # Decrement the counter


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
my_number = int(input('Input a number: '))
factorial = 1
while my_number > 0:
    factorial *= my_number  # Multiply by current number
    my_number -= 1  # Decrease number
print(f"Factorial is {factorial}")


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
correct_password = 'leidoe07'
user_input = ""
while correct_password != user_input:
    user_input = input('Enter the password: ')
    if correct_password == user_input:
        print('Correct!')  # Exit loop on correct input
        break
    print('Incorrect password, try again.')


"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
my_number = int(input('Input a number: '))
sum_of_digits = 0
while my_number > 0:
    sum_of_digits += my_number % 10  # Add last digit
    my_number //= 10  # Remove last digit
print(f"Sum of digits is {sum_of_digits}")
