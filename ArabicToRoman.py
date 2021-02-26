# !/usr/bin/python
# coding=UTF-8
# Written by Suma Kori <suma.kori93@gmail.com>, February 2021

"""This script is used to perform Arabic to Roman translation.
- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""
from operator import itemgetter


items = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400)
     , ("D", 500), ("CM", 900), ("M", 1000)]


def arabic_to_roman(number):
    """This method is used to convert the arabic number to roman numeral

    :param number
    :type str
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
    while True:
        value = int(input("Please enter the input"))
        if value > 0:
            print(arabic_to_roman(value))
        else:
            print("please enter the value grater than zero")

if __name__ == "__main__":
    main()
