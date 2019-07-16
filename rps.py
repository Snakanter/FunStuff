#!/usr/bin/env python3

"""
File: rps.py
Name:

A rock-paper-scissors game against the CPU
Concepts covered: Random, IO, if/else, printing
"""

import random
import sys
import os

def main():
    # Code here
    print("READY FOR A GAME OF ROCK, PAPER, SCISSORS!?")
    
   
    PlayerChoice = input("Choose between options by typing first letter. (R = Rock. P = Paper. S = Scissors.) ")
    while ( PlayerChoice != "R" and PlayerChoice != "S" and  PlayerChoice != "P" ):
        PlayerChoice = input("Choose between options by typing first letter. (R = Rock. P = Paper. S = Scissors.) ")
    choice = ai_guess(PlayerChoice)
    checkWin(PlayerChoice, choice)








def ai_guess(PlayerChoice):
    # Code here
    #1 = rock 2 = paper 3 = scissors
    choice = random.randint(1,3)
    return choice
    


def checkWin(PlayerChoice, choice):
    # Code here
    if (PlayerChoice == "R") and (choice == 1):
        print("It's a tie!")
    elif (PlayerChoice == "R") and (choice == 2):
        print("You lose!")
    elif (PlayerChoice == "R") and (choice == 3):
        print("You win!")
    elif (PlayerChoice) == ("P") and (choice) == (1):
        print("You win!")
    elif (PlayerChoice) == ("P") and (choice) == (2):
        print("It's a tie!")
    elif (PlayerChoice) == ("P") and (choice) == (3): 
        print("You lose!")
    elif (PlayerChoice) == ("S") and (choice) == (1):
        print('You lose!')
    elif (PlayerChoice) == ("S") and (choice) == (2):
        print('You win!')
    elif (PlayerChoice) == ("S") and (choice) == (3):
        print("It's a tie!")
    else:
        print("")
    
if __name__ == "__main__":
    main()
    
    while True:
        awnser = input("Would you like to try again?")
        if awnser == "Yes":
            os.system("cls")
            main()
        else:
            break
