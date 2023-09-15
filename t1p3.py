""" Simple Guessing Game """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: September 2023

import random
from time import sleep # To pause at the end of the code

def main():
    """ Main function of the guessing game """
    # Generate a random number from 1 to 100 with step of 1
    # ex: if step was 2 then valid numbers would be 1,3,5,etc.
    random_num = random.randrange(1, 100, 1)
    retry = True
    while retry:
        retry = False
    try:
        guess = int(input("Please guess a random number between 1 and 100:\n"))
        if guess == random_num:
            print("You guessed correctly!")
        else:
            difference = random_num - guess
            # For absolute value
            if difference < 0:
                difference *= -1
            print("You were", difference, "off")
    except Exception:
        print("Please input an actual number")
        retry = True
    sleep(1) # So the file does not instantly close when it is finished running


if __name__ == "__main__":
    main()
