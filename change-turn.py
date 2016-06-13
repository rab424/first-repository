#Robert's Change Turn Program
"""
This program is designed to change turns from a player to a computer and vice versa.
"""
import time

turn = "Player"

def Change_Turn():
    global turn
    if turn == "Player":
        turn = "Computer"
        print("Turn successfully changed from Player to Computer\n")
    elif turn == "Computer":
        turn = "Player"
        print("Turn successfully changed from Computer to Player\n")
    else:
        print("There was an error, doofus")

while True:
    if turn == "Player":
        #This is where code would go
        while True:
            answer = input("""Would you like to swap turns?
Yes\tNo
""").capitalize()
            if answer == "Yes":
                Change_Turn()
                break
            elif answer == "No":
                print("Okay, take your time.\n")
                time.sleep(2)
            else:
                print("Please enter a valid response.\n")
    elif turn == "Computer":
        #This is where code would go
        print("Computer is thinking.\n")
        time.sleep(2)
        Change_Turn()
    else:
        print("There was a mistake")


