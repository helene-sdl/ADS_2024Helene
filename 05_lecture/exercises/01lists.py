"""
Exercises "Lists"
"""

"""
### List Initialization and Accessing Items ###

Create a list named "colors" containing at least five different colors as strings. 
Print the third color in the list.
"""

# Write your solution here
colors = ["green", "yellow", "blue", "purple", "red"]
print(colors[2])
"""
### List Mutability ###

Initialize a list of numbers from 1 to 5. Change the second number in the list to 10.
Print the modified list.
"""

# Write your solution here
numbers = [1, 2, 3, 4, 5]
numbers[4] = 10
print(numbers)
"""
### Append and Insert Method ###

Create an empty list named "pets". Use the append method to add "dog", "cat", and "bird" to the list.
Then use the insert method to add "lizard" at the second position in the list.
Print the updated list.
"""

# Write your solution here
pets = []
pets.append('dog')
pets.append('cat')
pets.append('bird')
pets.insert(1, 'lizard')

# for pet in pets:
# print(pet)
"""
### Removing Items ###

Given the list ['apple', 'banana', 'cherry', 'date'], write a program that removes 'banana' using the remove() method and 'date' using the pop() method. 
Print the final list after these operations.
"""

list_of_fruits = ['apple', 'banana', 'cherry', 'date']
list_of_fruits.remove('banana')
list_of_fruits.pop(2)
print(list_of_fruits)
# Write your solution here

"""
### Sort Method and Sorting Function ###

Create a list of integers like: [5, 2, 9, 1, 5, 6].
Sort this list using the sort() method and then print it.
Next, use the sorted() function on the list ['orange', 'apple', 'banana'] and print the result.
"""
list_int = [5, 2, 9, 1, 5, 6]
list_int.sort()
print(list_int)
list_of_unsorted_fruits = ['orange', 'apple', 'banana']
list_of_unsorted_fruits.sort()
print(list_of_unsorted_fruits)
# Write your solution here

"""
### Min, Max, and Sum Functions ###

Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Print the minimum, maximum, and sum of the list.
"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(list_of_numbers))
print(max(list_of_numbers))
print(sum(list_of_numbers))
# Write your solution here

"""
### Slicing Lists Without Step and With Step ###

Create a list of the first 10 even numbers. Slice and print the first half of the list.
Then, slice and print every second number from the sliced list.
"""

# Write your solution here
list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
sublist1 = list1[:5]
print(sublist1)
sublist2 = sublist1[::2]
print(sublist2)