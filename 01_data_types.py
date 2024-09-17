"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
my_float = 3.5
my_int = int(my_float)
# used the int() function to convert the float variable into an intager
print(my_float)
print(my_int)
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
my_number =int(input( "what is ur number    " ))
if my_number > 0 :
    print("Ur number is positive")
elif my_number < 0 :
    print("Ur number is negative")
else  :
    print("Ur number is Zero")  
# used the int() to ask  for  reader fo a number to input 
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
two_number = input(" Input an integer and a decimal (put a comma in between; no spaces) ")

two_number_list = two_number.split(",")

print(two_number_list)
print("integer: " + int(two_number_list[0]) )
print("decimal: " + float(two_number_list[1]))
print ("addition: "+ float(two_number_list[0]) + float(two_number_list[1]) )
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""