"""
Write a function named list_of_stars, which takes a list of integers as its argument.
The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

    ***
    *******
    *
    *
    **

"""
# Provide your solution here


def list_of_stars(list_of_integers: [int]) -> None:
    for i in list_of_integers:
        string = "*" * i
        print(string)


list_of_stars([3, 7, 1, 1, 2])


"""
Write a function named anagrams, which takes two strings as arguments. 
The function returns True if the strings are anagrams of each other. 
Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
"""


# Provide your solution here
def anagrams(word1: str, word2: str):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


print(anagrams("tame", "meta"))
print(anagrams("python", "java"))

"""
Write a function named sum_of_positives, which takes a list of integers as its argument. 
The function returns the sum of the positive values in the list.

    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result) # prints The result is 9

"""
# Provide your solution here


def sum_of_positives(list_of_integers):
    positive_numbers = [num for num in list_of_integers if num > 0]
    result = sum(positive_numbers)
    print("The result is", result)


sum_of_positives([1, -2, 3, -4, 5])



"""
Write a function named even_numbers, which takes a list of integers as an argument. 
The function returns a new list containing the even numbers from the original list.

    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    
    Prints:
        original [1, 2, 3, 4, 5]
        new [2, 4]
"""
# Provide your solution here


def even_numbers(list_of_integers):
    return [num for num in list_of_integers if num % 2 == 0]


my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)


"""
Write a function named list_sum which takes two lists of integers as arguments. 
The function returns a new list which contains the sums of the items at each index in the two original lists. 
You may assume both lists have the same number of items.

An example of the function at work:

    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
"""


# Provide your solution here
def list_sum(list1, list2):
    return [x + y for x, y in zip(list1, list2)]


a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))


for i in range(3, 7):
    print(i, end="")


numbers = list(range(2, 7))
print(numbers)

