
#Task 1
# text = ["Hello, world, my name is"]
# count = 0

# for char in text:
#     if char == "  ":
#        count += 1
#     print(count)

#Task 2

# print("give me a number")
# n = int(input())

# for num in range(1, n+1):
#     if num % 2 <= 0:
#         print(num, "is even.")
#     else :
#         print(num, "is odd.")

#Task 3

# num = int(input("Enter an integer: "))
# if num < -1:
#   print("No negative numbers.")
# else:
#   result = num
#   for i in range(1, num ):
#     result *= i  


#   print("Factorial of " , num , "is" , result)

#Task 4

attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password:")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
    else:
        print("Incorrect password")

    if attempts = 3:
        print("Too many attempts")
        break




