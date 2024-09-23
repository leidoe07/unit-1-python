

import math
first_number = int(input('what is your first number:'))

second_number =int(input('what is your second number:'))

print(
    'Select operation:'
'1. Addition'
'2. Subtraction'
'3. Multiplication'
'4. Division'
'5. Floor Division'
'6. Exponential'
'7. Remainder')

the_operation = int(input('Enter choice:'))

if the_operation == 1:
    print(first_number , " + " , second_number )
    the_result = first_number + second_number
    print('result : ' , the_result)

if the_operation == 2:
    print(first_number + " - " + second_number )
    the_result = first_number - second_number
    print('result : ' , the_result)