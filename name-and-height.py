#Robert's Name and Height program
"""
This is a simple program saving the users inputted name and height and repeating it back to them
"""

name = input("What is your name?\n").capitalize()
height = float(input("What is your height?(in feet)\n"))
print("So your name is %s and you are %.1f feet tall?" % (name, height))
