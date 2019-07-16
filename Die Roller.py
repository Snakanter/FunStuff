import random

def main():
    awnser = input("Would you like to roll a 20 sided die? Y/N.")
    if awnser == Y:
        rand = random.randint(1,20)
        print("You rolled a" + rand + "!")
    if awnser == N:
        print("Ok.")
    Else:
        print