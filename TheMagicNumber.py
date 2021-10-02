########################################################################################################################################
### NewLight - The Magic Number.
### The magic number generates a random number between 1 and 10, the user needs to guess the number.
### The user has a limited number of lives (NB_LIVES)
### If the user input is greater or lower than magic number terminal output will notify the user.
########################################################################################################################################
import random

###### ask_number function is responsible for the user for input - converting to int, and managing exceptions #####
def ask_number(nb_min, nb_max):
    #number_str = input("What is the Magic Number between " + nb_min + "and " + nb_max) ## this gives concatination error, why?
    number_int = 0
    while number_int == 0:
        number_str = input(f"What is the magic number (between {nb_min} and {nb_max}?) ")
        try:
            number_int = int(number_str)
        except:
            print("Must be a number!")
        if number_int < nb_min or number_int > 10:
            print("Error, you must enter a number between 1 and 10")
            number_int = 0
    return number_int

##### Variables #####
MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 5
number = 0
lives = NB_LIVES

##### Main loop is responsible for updating user with the number of lives left, greater/lower status, and if he won/lost #####
while not number == MAGIC_NUMBER and lives > 0:
    print(f"You have {lives} lives!")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number < MAGIC_NUMBER:
        print("The Magic Number is GREATER")
        lives -= 1
    elif number > MAGIC_NUMBER:
        print("The Magic number is LOWER")
        lives -= 1
    else:
        print("You Won!")
if lives == 0:
    print("You lost!")
    print(f"The magic number was {MAGIC_NUMBER}")