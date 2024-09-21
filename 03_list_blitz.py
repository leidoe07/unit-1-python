"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
the_elements = ['kai', 'lloyd', 'nya', 'jay']
# Created a list named `the_elements` with elements ['kai', 'lloyd', 'nya', 'jay'] and printed it.

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated list.
"""
the_elements.append('master wu')
print(the_elements)
# Used `append()` to add the element 'master wu' to the end of `the_elements` and printed the updated list.

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the updated list.
"""
the_elements.remove('jay')
print(the_elements)
# Used `remove()` to delete the element 'jay' from `the_elements` and printed the updated list.

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. Print the updated list.
"""
the_elements[0] = 'cole'
print(the_elements)
# Updated the element at index 0 from 'kai' to 'cole' using direct indexing and printed the updated list.

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print the updated list.
"""
the_elements_2 = ['zane', 'skylar', 'P.I.X.A.L.']
the_elements.append(the_elements_2)
print(the_elements)
# Used `append()` to add the list ['zane', 'skylar', 'P.I.X.A.L.'] as a single element to `the_elements` and printed the updated list.

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated list.
"""
del the_elements[3]
print(the_elements)
# Used `del` to delete the element at index 3 (the appended list) from `the_elements` and printed the updated list.

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list.
Then print out the new variable.
"""
the_last = the_elements[0:2]
print(the_last)
# Created a new list `the_last` containing the first two elements of `the_elements` (['cole', 'lloyd']) and printed it.

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print the updated list.
"""
the_first = ['garmadon', 'wu']
the_best = the_last + the_first
print(the_best)
# Combined the lists `the_last` (['cole', 'lloyd']) and `the_first` (['garmadon', 'wu']) into a new list `the_best` and printed the result.
