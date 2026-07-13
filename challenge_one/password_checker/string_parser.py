""" String Parser by Violet Cat 39 """
""" A Helper function/class to parse each character in a string """

def parse_string(line):
    """
    Parses the String into a character array
    """
    character_list = []
    for item in line:
        character_list.append(item)
    return character_list

def main():
    """
    Main Function for manual testing
    """
    line = "Hello Wolrd!"
    print(parse_string(line))

if __name__ == "__main__":
    """
    Runguard
    """
    main()

