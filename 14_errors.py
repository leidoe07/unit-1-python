"""
Example 1: Division
"""
# This code attempts to divide two numbers. It handles two main issues:
# 1. Dividing by zero, which causes a ZeroDivisionError.
# 2. Entering a non-number as one of the inputs.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input. Please enter numbers.")


"""
Example 2: Opening Files
"""
# This function tries to read a file. If the file doesn't exist or an I/O error occurs,
# it will catch that and provide a friendly message. The file will still be closed
# even if something goes wrong, thanks to the `finally` block.

def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print("Error: An I/O error occurred.")
    finally:
        try:
            file.close()  # always attempts to close the file if it was opened
        except NameError:
            pass  # skips closing if the file was never opened


"""
Example 3: List Items
"""
# This function retrieves an item from a list at a specified index. It handles the case
# where an index is out of bounds or if the provided index is of the wrong type.

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    except IndexError:
        print(f"Error: Index {index} is out of range.")
    except TypeError:
        print("Error: Invalid index type.")


"""
Example 4: Dictionaries
"""
# This function looks up a key in a dictionary. If the key is missing, it handles that
# with a `KeyError`, and also ensures the key type is valid.

def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print("Value:", value)
    except KeyError:
        print(f"Error: Key '{key}' not found in dictionary.")
    except TypeError:
        print("Error: Invalid key type.")


"""
Example 5: Else/Finally
"""
#  an else block has been added to handle the scenario where no exceptions occur, and a `finally` block ensures a cleanup action is taken, whether an error occurs or not.

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("File contents:", contents)  # this runs only when no exception occurs
    finally:
        print("Finished processing file.")  # always runs, whether there's an error or not
