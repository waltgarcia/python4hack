# -*- coding: utf-8 -*-
"""Password generator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TVPtRpex72QeAEDd7tN_5wCmkVcywO30
"""

import random
import string
import sys

def generate_password(length=12):
    # Define character sets for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = random.choices(all_characters, k=length)

    # Convert the list of characters to a string
    password_str = ''.join(password)

    return password_str

def main():
    # Get the desired password length from the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 passwordgenerator.py <password_length>")
        return

    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()