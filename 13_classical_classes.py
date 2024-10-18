"""
Task 1: People Class
"""
# Define a class called Person with attributes name and age.
# A method to introduce the person is also created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Create a new object and call the introduce method
person1 = Person("Beyonce", 30)
person1.introduce()


"""
Task 2: Animals Speak
"""
# Create a base class Animal with an empty method called speak.
# Two subclasses, Dog and Cat, are defined, each with its own speak method.

class Animal:
    def speak(self):
        pass  # This method is meant to be overridden by subclasses

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Create objects using the subclasses and call the speak method
dog = Dog()
cat = Cat()

dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!


"""
Task 3: Banking
"""
# Create a class BankAccount with attributes balance and owner.
# Methods for depositing and withdrawing money are included.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance =  balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# Test the methods with instances of the class

account = BankAccount("John Doe", 100)
account.deposit(50)  # Output: Deposited 50. New balance: 150
account.withdraw(70)  # Output: Withdrew 70. New balance: 80
account.withdraw(120)  # Output: Insufficient funds!
