# -*- coding: utf-8 -*-
"""Passphrase generator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L9Elb1-WkZHL3KBfKBr-NPu-HMKDoNsD
"""

import random
import sys

def generate_passphrase(word_list, num_words=3):
    # Select random words from the given word list
    passphrase = random.sample(word_list, num_words)

    # Capitalize the first letter of each word
    passphrase = [word.capitalize() for word in passphrase]

    # Convert the list of words to a string, joined by "*"
    passphrase_str = '*'.join(passphrase)

    return passphrase_str

def main():
    # Example word list for medicine
    medical_terms = [
        "diagnosis", "treatment", "patient", "symptom", "medication",
        "physician", "nurse", "hospital", "surgery", "anatomy",
        "cardiology", "oncology", "neurology", "dermatology", "radiology",
        "pharmacy", "laboratory", "vaccine", "infection", "rehabilitation",
        "pediatrics", "gastroenterology", "urology", "obstetrics", "gynecology",
        "orthopedics", "emergency", "consultation", "prescription"
    ]

    # Get the desired number of words for the passphrase from the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 passphrasegenerator.py <num_words>")
        return

    try:
        num_words = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate the passphrase
    passphrase = generate_passphrase(medical_terms, num_words)

    # Display the generated passphrase
    print("Generated Passphrase:", passphrase)

if __name__ == "__main__":
    main()