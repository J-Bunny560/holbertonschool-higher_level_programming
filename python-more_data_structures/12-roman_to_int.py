#!/usr/bin/python3

def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    for i in range(len(roman_string)):
        if (i + 1 < len(roman_string) and
                roman_numerals[roman_string[i]] <
                roman_numerals[roman_string[i + 1]]):
            result -= roman_numerals[roman_string[i]]
        else:
            result += roman_numerals[roman_string[i]]

    return result
