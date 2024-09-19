"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
the_elements = ['kai','lloyd','nya','jay']
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
the_elements.append('master wu')
print(the_elements)
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
the_elements.remove('jay')
print(the_elements)
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
the_elements[0] = 'cole'
print(the_elements)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
the_elements_2 = ['zane','skylar','P.I.X.A.L.']
the_elements.append(the_elements_2)
print(the_elements)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del the_elements[3]
print(the_elements)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
the_last = the_elements[0:2]
print(the_last)
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
the_first = ['garmadon','wu']
the_best = the_last + the_first
print (the_best) 