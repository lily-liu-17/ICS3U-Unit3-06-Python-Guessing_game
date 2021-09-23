#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This lets user guess a number
# Program will say right or wrong and give answer

import random


def main():
    # This lets user guess a number
    some_variable = random.randint(1, 9)  # a number between 1 and 9
    guess_number = input("Enter a number between 1-9 : ")

    try:
        # input
        guess_number = int(guess_number)
        # process and output
        if guess_number == some_variable:
            print("You guessed correctly!")
        else:
            print("You guessed wrong!")
            print("The correct answer is {0}".format(some_variable))
    except Exception:
        print("Not an integer")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
