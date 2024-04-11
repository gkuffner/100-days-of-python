import sys
import random

def main():
    print("Welcome to the Treasure Island.\nYour mission is to find the treasure!")
    cross = input("You are in a cross. Do you want to go 'left' or 'right'?\n")
    if random.randint(0, 1):
        print("You walked away from the cross sucessfully!")
    else:
        print("You fell off a cliff! Game over :c")
        sys.exit()

    lake = input("You arrived in a lake. Do you want to 'swin' or to 'wait' for a boat?\n")
    if random.randint(0, 1):
        print("You've crossed the lake sucessfully!")
    else:
        print("You fell off a cliff! Game over :c")
        sys.exit()

    door = input("What door do you choose? 'blue', 'red' or 'green'?\n")
    if random.randint(0, 2) == 1:
        print("You've gone through the door sucessfully!\nYou found the treasure of knowledge!")
    else:
        print("You fell off a cliff! Game over :c")
        sys.exit()

if __name__ == "__main__":
    main()
