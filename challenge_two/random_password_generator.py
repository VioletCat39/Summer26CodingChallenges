""" Random Password Generator by VioletCat39 """

"""
Generates a random password
"""

import random
import character_generator
import password_check

def generate_password():
    """
    This function generates a random password with a random length
    """
    while (True):
        length = random.randint(12,24)
        password = ""
        for i in range(length):
            password += character_generator.get_random_char()
        if password_check.check_valid(password):
            return password
        
def main():
    """
    Main function for manual testing
    """
    print(generate_password())

if __name__ == "__main__":
    main()