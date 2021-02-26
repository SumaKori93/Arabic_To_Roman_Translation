# !/usr/bin/python
# coding=UTF-8
# Written by Suma Kori <suma.kori93@gmail.com>, February 2021

"""This script is used to perform Arabic to Roman translation.
- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""
from operator import itemgetter

# tuples which contains Integer along with their roman representation
items = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50), ("XC", 90), ("C", 100),
         ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)]


def arabic_to_roman(number):
    """This method is used to convert the arabic number to roman numeral

    :param: number
    :type: str

    """

    roman_numeral = ''
    i = 12
    while number != 0:
        roman = list(map(itemgetter(0), items))
        arabic = list(map(itemgetter(1), items))
        if arabic[i] <= number:
            roman_numeral += roman[i]
            number -= arabic[i]

        else:
            i = i-1

    return roman_numeral


def main():
    """This is the main method.

    1. Check if given number is numeric
    2. Check if given number is anything other than numeric. If q then quit.
    """

    while True:
        value = input("Please enter the input. Enter q to quit")
        if value.isnumeric():
            if int(value) > 0:
                print(arabic_to_roman(int(value)))
            else:
                print("please enter the value grater than zero")
        elif value == 'q' or value == 'Q':
            break
        else:
            print("please enter a valid number.")


if __name__ == "__main__":
    main()
