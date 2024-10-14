
import math  # Not needed right now, but could be useful for other math functions later

# Ask for the first number (can be a decimal, so using float)
first_number = float(input('What is your first number: '))

# Ask for the second number (also allowing decimals)
second_number = float(input('What is your second number: '))

# Display available operations for the user to choose from
print(
    'Select operation:\n'
    '1. Addition\n'
    '2. Subtraction\n'
    '3. Multiplication\n'
    '4. Division\n'
    '5. Floor Division\n'
    '6. Exponential\n'
    '7. Remainder\n'
)

# User inputs the choice for the operation
the_operation = int(input('Enter choice: '))

# Perform the operation based on the user's choice
if the_operation == 1:  # Addition
    print(first_number, " + ", second_number)  # Display the operation
    the_result = first_number + second_number  # Perform addition
    print('Result:', the_result)  # Output the result

elif the_operation == 2:  # Subtraction
    print(first_number, " - ", second_number)  # Display the operation
    the_result = first_number - second_number  # Perform subtraction
    print('Result:', the_result)

elif the_operation == 3:  # Multiplication
    print(first_number, " * ", second_number)  # Display the operation
    the_result = first_number * second_number  # Perform multiplication
    print('Result:', the_result)

elif the_operation == 4:  # Division
    if second_number != 0:  # Check to prevent division by zero
        print(first_number, " / ", second_number)  # Display the operation
        the_result = first_number / second_number  # Perform division
        print('Result:', the_result)
    else:
        # Handle division by zero case
        print("Error: Division by zero is not allowed.")

elif the_operation == 5:  # Floor Division (division, rounded down)
    if second_number != 0:  # Check for division by zero
        print(first_number, " // ", second_number)  # Display the operation
        the_result = first_number // second_number  # Perform floor division
        print('Result:', the_result)
    else:
        # Handle floor division by zero case
        print("Error: Division by zero is not allowed.")

elif the_operation == 6:  # Exponent (power operation)
    print(first_number, " ** ", second_number)  # Display the operation
    the_result = first_number ** second_number  # Perform exponentiation
    print('Result:', the_result)

elif the_operation == 7:  # Remainder (modulus operation)
    if second_number != 0:  # Check for division by zero
        print(first_number, " % ", second_number)  # Display the operation
        the_result = first_number % second_number  # Perform remainder operation
        print('Result:', the_result)
    else:
        # Handle modulus by zero case
        print("Error: Division by zero is not allowed.")

else:
    # Handle case where user inputs an invalid operation
    print("Invalid operation. Please select a valid option (1-7).")

# End of the program
print("\nThank you for using the calculator.")
