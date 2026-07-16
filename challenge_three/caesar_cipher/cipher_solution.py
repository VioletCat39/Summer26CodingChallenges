"Caesar Cipher by VioletCat39"

import time

UPPERCASE_MINIMUM = 65
UPPERCASE_MAXIMUM = 90
LOWERCASE_MINIMUM = 97
LOWERCASE_MAXIMUM = 122

def shift(letter, key):
    """
    In order to shift the letter, we need to:
    1) Instantiate a placeholder value for the ascii/unicode "number" of the new letter we are trying to make
    2) Create a value where the given letter is transferred into its ascii value, using int(ord())
    3) Compare it to make sure it is within either the capital or lowercase minimum/maximum, and therefore a valid letter (return the letter if it is not)
    If the key is a positive value:
    4) If the letter is less than the capital maximum and with the shift is still less than, apply the shift directly.
    5) If the letter is less than the capital maximum but with the shift applied is greater than the capital maximum, 
        Apply this formula to shift the value: (letter_ascii + shift - 1) - CAPITAL_MAXIMUM
        Ex: Suppose the given letter's ascii value is 88 ("X"), and we want to shift by 5 (XYZ loops back to ABC, where "C" is X shifted forward by five)
            This formula takes 88, adds 5 to the shift value, then subtracts the maximum ascii value and one,
            Which gives a total shift of 2.
            This is then applied to the minimum value, which gives the ascii result for "C"
    6) If the letter is less than the lowercase maximum and with the shift is still less than, apply the shift directly.
    7) If the letter is less than the lowercase maximum but with the key applied becomes greater than the lowercase maximum,
        Apply the same formula as step 5, adjusted for the lowercase values.
    If the key is a negative value:
    8) Apply similar logic as above, but instead for cases where the shift exceeds the minimum, take the minimum value and subtract (letter + shift + 1) to get the new shift value 

    9) This function returns the new letter using str(chr())
    """
    # Create Variable for shifted Letter Number
    new_letter_int = 0
    # Create variable for given letter ascii value
    letter_ascii_value = int(ord(letter))
    # Create variable for the returned/shifted letter
    shifted_letter = letter

    # Check to see if key is within one of the two bounds
    is_in_domain = (letter_ascii_value >= UPPERCASE_MINIMUM and letter_ascii_value <= UPPERCASE_MAXIMUM) or (letter_ascii_value >=LOWERCASE_MINIMUM and letter_ascii_value <= LOWERCASE_MAXIMUM)
    if is_in_domain:
        if letter_ascii_value <= UPPERCASE_MAXIMUM and (letter_ascii_value + key) <= UPPERCASE_MAXIMUM:
            new_letter_int = int(letter_ascii_value + key)
            shifted_letter = str(chr(new_letter_int))
        elif letter_ascii_value <= UPPERCASE_MAXIMUM and(letter_ascii_value + key) > UPPERCASE_MAXIMUM:
            leftover = (letter_ascii_value + key - 1) - UPPERCASE_MAXIMUM
            new_letter_int = UPPERCASE_MINIMUM + leftover
            shifted_letter = str(chr(new_letter_int))
        elif letter_ascii_value <= LOWERCASE_MAXIMUM and (letter_ascii_value + key) <= LOWERCASE_MAXIMUM:
            new_letter_int = int(letter_ascii_value + key)
            shifted_letter = str(chr(new_letter_int))
        elif letter_ascii_value <= LOWERCASE_MAXIMUM and (letter_ascii_value + key) > LOWERCASE_MAXIMUM:
            leftover = (letter_ascii_value + key - 1) - LOWERCASE_MAXIMUM
            new_letter_int = LOWERCASE_MINIMUM + leftover
            shifted_letter = str(chr(new_letter_int))
    
    # Always returns a value. If not in bounds it will return the given letter
    return shifted_letter


def decode(message, key):
    """ encodes the message given a message and key """
    encoded_message = ""
    for letter in message:
        encoded_message += shift(letter, key)

    return encoded_message

def main():
    ciphertext = input("Please Enter the Encrypted Password: ")
    key = 0
    while key < 26:
        print("Key:", key,"\nPassword: ",decode(ciphertext, key))
        key += 1
        time.sleep(0.5)

if __name__ == "__main__":
    main()