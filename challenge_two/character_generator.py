""" Random Character Generator by Violet Cat 39 """

import string
import random

ACCEPTABLE_CHARS = list(string.ascii_letters + string.digits + string.punctuation)

def get_random_char():
    """
    This function generates a random character
    """
    index = random.randrange(0, len(ACCEPTABLE_CHARS))
    return ACCEPTABLE_CHARS[index]

def main():
    """
    Main function to test elements of code manually
    """
    print(ACCEPTABLE_CHARS)
    for i in range(10):
        print(get_random_char())


if __name__ == "__main__":
    """
    Runguard (As recommended by local Soft Dev Professors near you!)
    """
    main()