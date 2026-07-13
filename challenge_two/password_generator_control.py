""" User Length - Auto Generated Password by VioletCat39 """
"""
Makes a random password given a user specified length
"""

import character_generator
import password_check

def generate_password(length):
    """
    This function generates a random password with a random length
    """
    while (True):
        password = ""
        for i in range(length):
            password += character_generator.get_random_char()
        if password_check.check_valid(password):
            return password
        
def main():
    """
    Main function for manual testing
    """
    length = 0
    length = int(input("Please enter password length: "))
    print(generate_password(length))

if __name__ == "__main__":
    main()