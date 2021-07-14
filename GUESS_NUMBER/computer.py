#Import the built in python library random
import random

#Defining a function
def guess(x):
    random_no = random.randint(1,x) #randint is another inbuilt library to randomly prompt numbers
    guess = 0 #Initially assign it to 0

    #A while loop to check if the number is not guessed correctly
    while guess != random_no:
        guess = int(input(f"Guess a number between 1 and {x}.. :"))

        #Using if condition to prompt relevant feedback
        if guess < random_no:
            print("Oops!!.Wrong guess!!. The number is very small")
        elif guess > random_no:
            print("Oops!!.Wrong guess!!. The number is quite large")

    #If the number is correct print it out of the while loop
    print(f"WoW!! You Won!!.You guessed the number {random_no} correctly!!...")

#Call the function and assign any value
guess(100)