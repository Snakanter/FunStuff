import random


def main():
    randnum = random.randint(1,10)
    tries=5
    while(tries>0):
        guess = int(input("I have thought of a number between one and ten. Can you guess what it is?"))
        
        if (guess == randnum):
            print("You did it! And you win... nothing !")
            break
     
        else:
            print("Nope!")
            tries = tries -1
            print("You have " + str(tries) + " lives left") 

    if (tries==0):
        print("Game Over.")
if __name__ == "__main__":
    main()
