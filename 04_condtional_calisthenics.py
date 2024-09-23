'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
my_int = 11
if my_int > 10 and my_int == 10 :
    print(True)
else:
    print(False)

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
student_age = int(input('how old are you'))
student_status = input('are you a student').strip
valid_status = str('yes')
if student_age < 18 or student_status == valid_status:
    print('Ticket Price is $10')
else:
    print('Ticket Price is $20')

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruit_name = input('name a fruit')
fruit_list = ['apple','tomato','banana','orange']
if fruit_name in fruit_list:
    print('Yes, that fruit is in the list.')
elif fruit_name not in fruit_list:
    print('No, that fruit is not in the list.')
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
the_year = 2000
if the_year % 100 == 0:
    print('this is a century year') 
elif the_year % 400 == 0 :
    print(' this is a leap year')

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''