#Import the built in python library random
import random

#Defining a function
def computer_guess(x):
    small = 1 #Initially assign it to 1 the starting number
    large = x
    result = '' #Initially assign it to an empty string

    #A while loop to check if the number is not guessed correctly
    while result != 'c':

        #If condition to check whether the number is correct
        if small != large:
            guess = random.randint(small,large) #Prompts random numbers if small and large are different
        else:
            guess = small #It can be large or small as the number is correct

        result = input(f"Is {guess} too Large (L) or too Small (S) or Correct (C) ? : ").lower() #In order to handle lower case user input
        if result == 'l':
            large = guess-1
        elif result == 's':
            small = guess+1

    #If the number is correct print it out of the while loop
    print(f"Wohoo!!! The computer guessed your number {guess} correctly.")

#Call the function and assign any value
computer_guess(200)
