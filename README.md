# Arabic_To_Roman_Translation

## Definition of the task

Write a function which turns an Arabic number into a Roman numeral in its minimal form using the "standard" subtractive notation

## Solution

items = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400)
     , ("D", 500), ("CM", 900), ("M", 1000)]

The above list has the set of tuples which contains Integer along with their roman representation.

step 1: Find the largest number from the list which is less than or equal to given input.

step 2: Write down the Roman numeral of this number and Substract its value from the input number.

step 3: Repeat step 1 and 2 until we left with zero
