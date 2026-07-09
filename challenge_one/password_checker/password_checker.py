""" Password Strength Checker 
    Checks to see the strength of a given password dependent on multiple parameters """

from string_parser import *

ASCII_UPPER_MAX = 90
ASCII_UPPER_MIN = 65
ASCII_LOWER_MAX = 122
ASCII_LOWER_MIN = 97
NUMBER_SET = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
ALLOWED_SPECIAL_CHARACTERS = {'!', '@', '#', '$', '%', '^', '&', '(', ')', ',', '.', '?', '_', '-', '+', '=', '\'', '\"', '<', '>', '|', '/', '\\', '*', ':', ';', '{', '}', '[', ']'}

def get_array(password):
    """
    Uses the helper method to parse the string into an array
    """
    return parse_string(password)

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
    Checks to see if the password has 3 or more of the same character in a row
    """
    letter_second_previous = ''
    letter_previous = ''

    for letter in password:
        if (letter == letter_previous) and (letter == letter_second_previous):
            return True
        letter_second_previous = letter_previous
        letter_previous = letter

    return False

def size_checker(password):
    """
    Checks to see if the password is in an acceptable size range (8 to 32)
    """
    length = len(password)
    if length >= 8:
        if length <=32:
            return True
        
    return False

def above_ten_characters(password):
    """
    Checks to see if the password is above ten characters
    """
    length = len(password)
    if length >= 10:
        return True
        
    return False

def get_strength(password):
    """
    Helper function to calculate password strength as a numeric value from previous tests
    """
    score = 0
    if has_lowercase(password) and has_uppercase(password):
        score+=1
    if has_special(password):
        score+=1
    if has_numeric(password):
        score+=1
    if above_ten_characters(password):
        score+=1
    if score == 4:
        score+=1
    if recurrence_limit(password):
        score -=1
    return score


def main():
    """
    Main Function
    """
    password_strength = 0
    password = input("Please enter password: ")
    password_length = get_array(password)
    if size_checker(password) != True:
        print("Invalid Password!")
    else:
        print(get_strength(password))
    print("Error! Code not yet complete!")

if __name__ == "__main__":
    """
    Runguard
    """
    main()