#!/usr/bin/env python3

# Created By: Nolan Shami
# Date: October 27th, 2022
# This program asks the user for a number between 1-12
# and associates the number with the corresponding
# month back to the user.
from select import select


def main():
    user_month = int(input("Enter a number for a month between 1-12: "))

    match user_month:
        case 1:
            print("1 is for January!")
        case 2:
            print("2 is for February!")
        case 3:
            print("3 is for March!")
        case 4:
            print("4 is for April!")
        case 5:
            print("5 is for May!")
        case 6:
            print("6 is for June!")
        case 7:
            print("7 is for July!")
        case 8:
            print("8 is for August!")
        case 9:
            print("9 is for September!")
        case 10:
            print("10 is for October!")
        case 11:
            print("11 is for November!")
        case 12:
            print("12 is for December!")
        case _:
            print(str(user_month) + " is not in between 1 and 12!")


if __name__ == "__main__":
    main()
