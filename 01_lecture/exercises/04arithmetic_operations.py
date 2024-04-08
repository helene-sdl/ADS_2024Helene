"""
Write a program which asks the user for a number.
The program then prints out the number multiplied by five.
Example:
    Please type in a number: >> 7
    7 times 5 is 35
"""
# Write your solution here ???


number = float(input("Please enter a number: \n"))
result = number * 5
print("The result of multiplying", number, "by five is:", result)




"""
Write a program which asks the user for their name and year of birth. 
The program then prints out a message as follows:
    What is your name? >> Frances Fictitious
    Which year were you born? >> 1990
    Hi Frances Fictitious, you will be 34 years old at the end of the year 2024
"""
# Write your solution here
name = input("What is your name? \n")
year = int(input("Which year were you born? \n"))
print("Hi," + name + " " + f'you will be {2024 - year} ' + "years old at the end of the year 2024.")



"""
Write a program which asks the user for a number of days. 
The program then prints out the number of seconds in the amount of days given.
Example:
    How many days? >> 7
    Seconds in that many days: >> 604800
"""
# Write your solution here

days = int(input("Please enter the number of days: \n"))
seconds_in_a_day = 24 * 60 * 60
total_seconds = days * seconds_in_a_day
print("There are", total_seconds, "seconds in", days, "days.")

"""
This program asks the user for three numbers. 
The program then prints out their product, that is, the numbers multiplied by each other. 
There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it. 
Please fix it.
"""
# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)


"""
Write a program which asks the user for four numbers. 
The program then prints out the sum and the mean of the numbers.
Example: 
    Number 1: >> 2
    Number 2: >> 1
    Number 3: >> 6
    Number 4: >> 7
    The sum of the numbers is 16 and the mean is 4.0
"""
# Write your solution here
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
number4 = int(input("Please type in the fourth number: "))
sum_total = number1 + number2 + number3 + number4
mean = sum_total / 4
print("The sum of the three numbers is " + str(sum_total) + " and the mean is " + str(mean))


"""
Write a program that asks the user for a three-digit number input.
Reverse the given number by using modulo and division operator.
Example:
    Enter a number: >> 123
    The reversed number is: >> 321
"""
# Write your solution here
n1 = int(input("Please type in a three-digit number: "))
print(n1%10)
print(n1//10%10)
print(n1//100)

print(f"{n1%10}{n1//10%10}{n1//100}")


