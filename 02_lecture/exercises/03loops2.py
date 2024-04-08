

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









