# Created by:   Patrick Archer
# Date:         13 December 2018
# Copyright to the above author. All rights reserved.

"""
Directions - COMPLETE:
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them if they can vote and how long until they can/how long they have been able to.

Extras - COMPLETE:
(1 - DONE) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
    (Hint: order of operations exists in Python)
(2 - DONE) Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button).
"""

# ################################################# start_funcs

# func to handle performing calculations and printing values
def calcVals(name, age):
    # if user did enter their age as a valid integer, proceed as normal
    try:
        age = int(age)
        if (age < 18):
            print(name + ", you cannot vote yet. You have " + str(18 - age) + " years left.\n")
        elif (age >= 18):
            print(name + ", you can vote, and have been able to for " + str(age - 18) + " years.\n")
        else:
            print("An error has occurred. Ending program to prevent further catastrophe.\n")
    # if user did not enter their age as an integer, catch error and exit program safely
    except (ValueError):
        print("ERROR: You have entered an invalid age. Ending program to prevent further catastrophe.\n")

# ################################################# end_funcs/start_main

# DEPRECATED: Take user's name and age and store to corresponding vars
#userName = raw_input("\nPlease enter your name. Press \"Enter\" when ready.\n")
#userAge = raw_input("\nPlease enter your age. Press \"Enter\" when ready.\n")

# PYTHON v3.7: Take user's name and age and store to corresponding vars
userName = input("\nPlease enter your name. Press \"Enter\" when ready.\n")
userAge = input("\nPlease enter your age. Press \"Enter\" when ready.\n")

# FOR EXTRA (1): prompt user for how many times they would like the statements printed
timesToPrint = input("\nHow many times would you like the output statements printed? Press \"Enter\" when ready.\n")

print("\n============\n") # for organization

# for the # of times the user specified, do...
try:
    timesToPrint = int(timesToPrint)    # convert str to int, under error-catching supervision
    for n in range(timesToPrint):   # print info the # of times user specified
        print("Iteration #" + str(n + 1) + ": ")
        calcVals(userName, userAge)
    print("============")   # for organization
except (ValueError):
    print("ERROR: You have entered an invalid print count value. RESULT: The output will be printed once.\n")
    print("Iteration #1: ")
    calcVals(userName, userAge)

# ################################################# end_main

