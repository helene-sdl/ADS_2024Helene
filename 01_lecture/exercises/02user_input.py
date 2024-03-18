"""
Write a program that asks for a user's name and then prints it twice

    What is your name? >> Leon
    Leon
    Leon
"""
# Write your solution here
name = input("What is your name?")
print(name)
print(name)

"""
 Write a program that asks for a user's name and then prints it out twice separated by exclamation marks

    What is your name? >> Leon
    !Leon!Leon!
"""
# Write your solution here
name = input("What is your name? \n")
print("!", name, "!", name, "!")

"""
Here is a program which should ask for three utterances and print them out, like so:

    The 1st part: >> hickory
    The 2nd part: >> dickory
    The 3rd part: >> dock
    hickory-dickory-dock!
"""

# Fix the code ??????????
part1 = input("What do you want to say first? \n")
part2 = input("What do you want to say then? \n")
part3 = input("What is the last thing you say? \n")

print(part1 + "-" + part2 + "-" + part3 + "!")

"""
Write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.

    Please type in a name: >> Mary
    Please type in a year: >> 1572
    
    
"""
# Write your solution here
name = input("What is the name? \n")
number = input("What is the year? \n")
print("Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was "
      "approaching the village. Only Mary could save the village's residents.")