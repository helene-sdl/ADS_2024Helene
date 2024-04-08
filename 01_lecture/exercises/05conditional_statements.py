"""
Write a program that asks the user for a number.
The program then determines if the number is even or odd and prints out an appropriate message.

Hint: For checking if the number is even or odd, use the Modulo operator:
remainder = number % 2

Example:

    Enter a number: >> 17
    The number 17 is odd.
"""
# Write your solution here
number = int(input("Please give me a number: \n"))
if number % 2:
    print("The number is uneven.")
else:
    print("The number is even.")


"""
Write a program that asks the user for their exam grade (as a percentage). 
The program then prints out the following message:

* If the grade is below 50%: "Unfortunately, you failed the exam."
* If the grade is 60% or above: "You passed the exam!"
* If the grade is higher or equal to 90: "You are excellent!"

Example:

    Enter your exam grade: >> 63
    You passed the exam!
"""
# Write your solution here
grade = int(input("Please enter the percentage you received on your exam: \n"))
if grade < 50:
    print("Unfortunately, you failed the exam.")
# probably rather over 50
if grade >= 60:
    print("You passed the exam!")
if grade >= 90:
    print("You are excellent!")
"""
Write a program that simulates a simple lunch ordering system. 

1. Ask the user if they want a sandwich, salad, or wrap.
2. If they want a sandwich, ask what kind (chicken, beef, veggie).
3. If they want a salad, ask what dressing (vinaigrette, ranch, caesar).
4. If they want a wrap, ask if they want it toasted.
5. Print a confirmation of their order choice.

Hint: You don't need to verify the user input. But if you want a challenge, try to repeat reading the user input
in case of invalid input. To do so, you might need to research a little bit about "loops" which will be 
covered later in this course :-)

Example:

    Would you like a sandwich, salad, or wrap? >> salad
    What kind of dressing would you like: vinaigrette, ranch, or caesar? >> ranch
    Your order: Salad with ranch dressing
"""
# Write your solution here
food = input("Welcome to our lunch ordering system! Would you like a sandwich, salad or wrap? \n")

if food == "salad":
    dressing = input("What kind of dressing would you like: vinaigrette, ranch, or caesar? \n")
    if dressing == "vinaigrette":
        print("Your order: Salad with vinaigrette dressing")
    elif dressing == "ranch":
        print("Your order: Salad with ranch dressing")
    elif dressing == "caesar":
        print("Your order: Salad with caesar dressing")

elif food == "sandwich":
    sandwich_kind = input("Would you like a chicken, beef or veggie sandwich? \n")
    if sandwich_kind == "chicken":
        print("Your order: A chicken sandwich")
    elif sandwich_kind == "beef":
        print("Your order: A beef sandwich")
    elif sandwich_kind == "veggie":
        print("Your order: A veggie sandwich")

elif food == "wrap":
    toasted = input("Do you want your wrap toasted? (Yes/No) \n")
    if toasted == "Yes":
        print("Your order: A toasted wrap")
    elif toasted == "No":
        print("Your order: A not toasted wrap")

else:
    print("Your input is invalid. Please try again.")
