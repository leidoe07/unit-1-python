"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
my_pass = "candylots07"
pass_word = input("what is the passord :").lower()

if my_pass == pass_word:
    print("password is correct")

else:
    print("password is incorrect")
#Used  the lower() function to  make whatever users input lower case so that it would not be sensitive.
"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
the_term = int(input("how old are you :"))
term_age = the_term.strip()
no_age = ""
if term_age == no_age :
    print("invalid")
else:
    print("valid")

# used the strip() functions so that whatever ever whitespace users input without actually adding a number would be invalid
"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
fav_pet = "My favorite pet is a cat"
new_pet = fav_pet.replace("cat",'dog')
print(new_pet) 

# used the the replace() fuction to replace the word 'cat' with 'dog'
"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
player_name = input(" what is ur name")
player_age = input("what is ur age")

player_sentence = f"{player_name} is {player_age} is years old."
print(player_sentence)
# used the format() function to input whatever  age and name users gave into the preset sentence
"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
numb_1 = 9
numb_2 = 4

numb_3 = numb_1 / numb_2

print (f"quotient: {numb_3 : .1f}")

#used format() function to limit the quotient to one decimal place