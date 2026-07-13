""" Password Checker mkII by VioletCat39 """
"""
Similar to challenge one, but instead follows the parameters in the about.txt for this challenge, and is more condensed
"""

import string

ASCII_UPPER_MAX = 90
ASCII_UPPER_MIN = 65
ASCII_LOWER_MAX = 122
ASCII_LOWER_MIN = 97
NUMBER_SET = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
ALLOWED_SPECIAL_CHARACTERS = {'!', '@', '#', '$', '%', '^', '&', '(', ')', ',', '.', '?', '_', '-', '+', '=', '\'', '\"', '<', '>', '|', '/', '\\', '*', ':', ';', '{', '}', '[', ']'}


def parse_string(line):
    """
    Parses the String into a character array (taken from challenge one)
    """
    character_list = []
    for item in line:
        character_list.append(item)
    return character_list

def has_uppercase(password):
    """
    Checks the parsed password for an uppercase character
    """
    for letter in password:
        if (ord(letter) >= ASCII_UPPER_MIN) and (ord(letter) <= ASCII_UPPER_MAX):
            return True
    return False

def has_lowercase(password):
    """
    Checks the parsed password for an lowercase character
    """
    for letter in password:
        if (ord(letter) >= ASCII_LOWER_MIN) and (ord(letter) <= ASCII_LOWER_MAX):
            return True
    return False

def has_numeric(password):
    """
    Checks the parsed password to see if it has a number
    """
    for letter in password:
        if letter in NUMBER_SET:
            return True
    return False
    

def has_special(password):
    """
    Checks to see if the password has a special character
    """
    for letter in password:
        if letter in ALLOWED_SPECIAL_CHARACTERS:
            return True
    return False

def recurrence_limit(password):
    """
    Checks to see if the password has 2 of the same character in a row
    """
    letter_previous = ''

    for letter in password:
        if (letter == letter_previous):
            return True
        letter_previous = letter

    return False

def check_valid(password):
    """
    This method checks to see if the password is valid given the parameters and characters
    True if it is valid, false if invalid.
    """
    parsed = parse_string(password)
    if not has_lowercase(parsed):
        return False
    if not has_uppercase(parsed):
        return False
    if not has_numeric(parsed):
        return False
    if not has_special(parsed):
        return False
    if recurrence_limit(parsed):
        return False

    return True

def main():
    """
    Main function for manual tests
    """

    print(check_valid("Password1234!"))
    print(check_valid("Wh4fins1!gheno"))

if __name__ == "__main__":
    main()