#!/usr/bin/env python

import hashlib

# Function to get user input in Python 3.x
def get_input(prompt):
    try:
        # For Python 3.x
        return input(prompt)
    except NameError:
        # For Python 2.x
        return raw_input(prompt)

questions = [
    "Q1: What is the deleted filename you need to find in previous snapshot?",
    "Q2: What is the encrypted message in the letter found in the snapshot?",
    "Q3: What is the decrypted text?",
]

# The hashes here are placeholders and should be replaced with the SHA256 hashes
# of the correct answers to the questions for the TrueNAS challenge
answers = [
    '6422ee9e9e3553223a24400e0499afa8df3802da',
    'cf6d4d68ac701b33c9e7a3460bcc0981e4554a81',
    '9b0bb6d5b4cafa9c9333c45e342095d2ba7f98ea'
]

def recursively_prompt_question(question, expected_hash):
    user_input = get_input(question + '\n> ').strip()
    if hashlib.sha1(user_input.encode()).hexdigest() == expected_hash:
        print("Correct! ... +10 points\n")
        return True
    else:
        print("Incorrect. Let's try again!\n")
        return recursively_prompt_question(question, expected_hash)

if __name__ == "__main__":
    score = 0
    for i in range(len(questions)):
        if recursively_prompt_question(questions[i], answers[i]):
            score += 10
    print('Success! Total score: ' + str(score))

