"""
Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Example:
    Width: >> 10
    Height: >> 3
    ##########
    ##########
    ##########
"""
# Write your solution here

width = int(input("Width: "))
height = int(input("Height: "))
print(width * '#')
while height > 1:
    print(width * '#')
    height -= 1


