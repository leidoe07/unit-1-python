
# Import the necessary modules from the datetime library
from datetime import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

# Get the current date and time
current_datetime = datetime.now()
# Print the current date and time
print("Current date and time:", current_datetime)


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

# Format the current date in MM/DD/YYYY format
formatted_date = current_datetime.strftime("%m/%d/%Y")
# Print the formatted date
print("Current date in MM/DD/YYYY format:", formatted_date)


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

# Define two date strings
date_string1 = "01/15/2024"  # January 15, 2024
date_string2 = "10/14/2024"  # October 14, 2024

# Convert the strings to datetime objects
date1 = datetime.strptime(date_string1, "%m/%d/%Y")
date2 = datetime.strptime(date_string2, "%m/%d/%Y")

# Calculate the difference in days between the two dates
difference = (date2 - date1).days
# Print the difference in days
print("Difference in days between the two dates:", difference)


"""
Exercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

# Ask the user for their birthdate in MM/DD/YYYY format
birthdate_str = input("Enter your birthdate (MM/DD/YYYY): ")
# Convert the input string to a datetime object
birthdate = datetime.strptime(birthdate_str, "%m/%d/%Y")

# Calculate the difference in years between the current date and the birthdate
today = datetime.now()
age = today.year - birthdate.year

# Adjust for whether the birthday has occurred this year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# Print the user's current age
print("Your current age is:", age)
