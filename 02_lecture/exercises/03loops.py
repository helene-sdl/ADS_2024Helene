from math import sqrt

"""
Write a program that prints out the message "hello world!" and then asks "shall we continue?"
until the user inputs "no". Then the program should print out "okay then" and finish.

Example:
    hello world!
    shall we continue? >> yes
    hello world!
    shall we continue? >> oui
    hello world!
    shall we continue? >> jawohl
    hello world!
    shall we continue? >> no
    okay then
"""
# Write your solution here

while True:
    print("hello world!")
    response = input("shall we continue?")
    if response == "no":
        print("Okay then")
        break

"""
Write a program which asks the user for integer numbers.

- If the number is below zero, the program should print out the message "invalid number".
- If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
- In either case, the program should then ask for another number.
- If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

To use the `sqrt` function in python add the following to the top of your file: 
    from math import sqrt
Then use it like:
    print(sqrt(9))
    
Example:
    Please type in a number: >> 16
    4.0
    Please type in a number: >> 4
    2.0
    Please type in a number: >> -3
    invalid number
    Please type in a number: >> 1
    1.0
    Please type in a number: >> 0
    Exiting...
"""

while True:
    number = int(input("Please type in a number:"))
    if number < 0:
        print("invalid number")
    elif number > 0:
        print(sqrt(number))
    elif number == 0:
        print("Exiting...")
        break

"""
This program should print out a countdown. However, the program doesn't quite work. Please fix it.
Hint: you can use the debugger of PyCharm to see how the program is executing.
"""
# Fix the code
number = 5
print("Countdown!")
while True:
    if number >= 0:
        print(number)
        number = number - 1
    if number == 0:
        break

print("Now!")

"""
Write a program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.

Examples:
    Year: >> 2023
    The next leap year after 2023 is 2024
    
    Year: >> 2024
    The next leap year after 2024 is 2028
"""
# Write your solution here ???
year = int(input("Please type in a year: "))

while True:
    year += 1
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The next leap year is:", year)
        break


"""
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.

Example:
  Please type in a word: >> Once
  Please type in a word: >> upon
  Please type in a word: >> a
  Please type in a word: >> time
  Please type in a word: >> there
  Please type in a word: >> was
  Please type in a word: >> a
  Please type in a word: >> girl
  Please type in a word: >> end
  Once upon a time there was a girl
"""
# Write your solution here
words = ""
attempts = 0

while True:
    word = input("Please type in a word:")
    print(word)
    attempts += 1
    words += word + " "
    if word == "end":
        print(words)
        break

"""
Change the program above so that the loop ends also if the user types in the same word twice in a row.
"""
# Write your solution here

prev_word = None
words = ""
while True:
    word = input("Please type in a word: ")
    print(word)
    if word == prev_word:
        print("You've entered the same word twice in a row. Exiting loop.")
        break
    words += word + " "
    if word == "end":
        print(words)
        break
    prev_word = word

"""
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in 0.

After reading the numbers the program should 
  - print out how many numbers were typed in
  - the sum of numbers entered
  - the mean of numbers entered
  - the number of positive and negative numbers entered
  
Example output
  Numbers typed in 4
  The sum of the numbers is 34
  The mean of the numbers is 8.5
  Positive numbers 3
  Negative numbers 1
"""
# Write your solution here    ???????????

numbers = []
positive_numbers = 0
negative_numbers = 0
while True:
    number = int(input("Please type in a number: "))

    if number == 0:
        break
    numbers.append(number)
    if number > 0:
        positive_numbers += 1
    elif number < 0:
        negative_numbers += 1

numbers_typed_in = len(numbers)
sum_numbers = sum(numbers)
mean_numbers = sum_numbers / numbers_typed_in if numbers_typed_in > 0 else 0

print("Numbers typed in " + str(numbers_typed_in))
print("The sum of the numbers is " + str(sum_numbers))
print("The mean of the numbers is " + str(mean_numbers))
print("Positive numbers " + str(positive_numbers))
print("Negative numbers " + str(negative_numbers))


"""
Largest Number

Write a program which asks the user for float numbers.
The program should keep asking for numbers until the user types in 0 or a negative number.
The program should then print the largest number.
If the first number entered is less than or equals to 0, the program should quit and print "no number entered".

DO NOT USE LISTS TO SOLVE THIS EXERCISE!

Examples:
  Number 1: >> 3
  Number 2: >> 4.67
  Number 3: >> 120.5
  Number 4: >> 70
  Number 5: >> 0
  The largest number is 120.5
  
  Number 1: >> -1.11
  No number entered.
"""
# Write your solution here

numbers = []
number = float(input("Please type in a number: "))
while True:
    if number <= 0:
        print("No number entered.")
        break
    number = float(input("Please type in a number: "))
    numbers.append(number)
    largest_number = max(numbers)
    if number <= 0:
        print("The largest number is " + str(largest_number))
        break




"""
Write a program that reads in an integer number (number of lines) and generates the subsequent output using 
two loops on the console (see below). 
If the input of numbers is smaller or equal to 0 an error message should be printed.

Examples:
  n: >> 4
  1
  2 3
  4 5 6
  7 8 9 10
  
  n: >> -1
  Invalid number!
"""
# Write your solution here
number_lines = int(input("Please type in the number of lines:"))
i = 1
current_number = 1
while i <= number_lines:
    j = 1
    while j <= i:
        print(current_number, end=" ")
        current_number += 1
        j += 1
    print()
    i += 1

while True:
    if number_lines <= 0:
        print("Invalid number")
        break
"""
Write a program that uses loops to create a pyramid of stars '*' on the console. 
The pyramid should have exactly 6 rows.
Example:
       *
      ***
     *****
    *******
   *********
  ***********
"""
# Write your solution here

rows = 6
i = 1
while i <= rows:
    j = 1
    while j <= rows - i:
        print(" ", end="")
        j += 1

    j = 1
    while j <= 2 * i - 1:
        print("*", end="")
        j += 1

    print()
    i += 1

"""
Write a program to calculate the average grade. The console reads in grades between 1 and 5 
until the number 0 is entered. If an invalid grade is entered, an error message is displayed, 
the grade is not counted and the prompt progresses. It is assumed that only integers are entered. 
At the end of the input, the grade average and the number of negatives (grade = 5) are output.

Example:
  Mark 1: >> 5
  Mark 2: >> 3
  Mark 3: >> 10
  Invalid mark!
  Mark 3: >> 1
  Mark 4: >> 5
  Mark 5: >> 0
  Average: 3.50
  Negative marks: 2
"""
# Write your solution here
grades = []
negative_grades = 0

while True:
    grade = int(input("Please enter a grade: "))

    if grade == 0:
        break
    elif grade < 1 or grade > 5:
        print("Invalid mark!")
        continue

    grades.append(grade)
    if grade == 5:
        negative_grades += 1

average_grade = sum(grades) / len(grades)
print("Average: " + str(average_grade))
print("Negative marks: " + str(negative_grades))





