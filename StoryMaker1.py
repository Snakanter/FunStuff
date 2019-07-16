def main():
    noun1 = input("I require a name.")
    job1 = input("What is their job?")
    verb1 = int(input("Please verify gender. 1 for Male and 2 for Female and 3 for other."))
    noun2 = input("I need another name.")
    verb2 = int(input("Verify gender in the same way as before."))
    place = input("I need a place")
                  
    
    
    
    if verb1 == 1:
        print("There was once a human that went by the name of" + noun1 + ". He was a simple man, working as a" + job1 +" in the town of YanderVille.")
    
    
    if verb1 == 2: 
        print("There was once a human that went by the name of" + noun1 + ". She was a simple woman, working as a" + job1 +" in the town of YanderVille.") 
    
    if verb1 == 3:
        print("There was once a human that went by the name of" + noun1 + ". They were a simple person, working as a" + job1 +" in .")

    
        
        
    
if __name__ == "__main__": 
    main()