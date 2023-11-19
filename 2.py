#!/usr/bin/env python
import ls
import hashlib
# Function to get user input in Python 3.x
def get_input(prompt):
    return input(prompt)

questions = [
    "Q1: We will check if you have already created your own NFS",
    "Q2: Can you create 'tartans' in nfstemp? (yes/no)",
    "Q3: What is your permission status in nfstemp (Hint: ls -al) (Format: -rwxr--r-x)",
    "Q4: We will check if you have already created your tartans@1",
    "Q5: What is your permission status for tartans@1"
]

answers = [
    '0',
    '9390298f3fb0c5b160498935d79cb139aef28e1c47358b4bbba61862b9c26e59',  
    'ea1376c4bdef73e77062dccac2f4daa9ff3e858fabf58273c2b23abda627bd91',
    '0',
    '3aa23883654649f8f3a024f73a84395b9310191b06febf8ff1ccaf2c3b8bb67d'
]

scores = [
    20,10,10,20,10
]

def recursively_prompt_question(index, expected_hash): 
    if index == 0:
        print(questions[i])
        user_input = get_input("Please press Enter to continue" + '\n> ').strip()
        return ls.is_nfs_existed()
        
    elif index == 1:
        print(questions[i])
        user_input = get_input('\n> ').strip()
        if hashlib.sha256(user_input.encode()).hexdigest() == expected_hash:
            return True
        else:
            return False
            
    elif index == 2:
        print(questions[i])
        user_input = get_input("\n> ").strip()
        if hashlib.sha256(user_input.encode()).hexdigest() == expected_hash:
            return True
        else:
            return False
            
    elif index == 3:
        print(questions[i])
        user_input = get_input("Please press Enter to continue" + '\n> ').strip()
        return ls.is_tartans_existed()
        
    elif index == 4:
        print(questions[i])
        user_input = get_input("\n> ").strip()
        if hashlib.sha256(user_input.encode()).hexdigest() == expected_hash:
            return True
        else:
            return False

if __name__ == "__main__":
    score = 0
    for i in range(len(questions)):
        result = False
        while recursively_prompt_question(i, answers[i]) == False:
            print("Ooops! The answer is incorrect.")
        print("Congrats! You get the correct answer.")
        score += scores[i]
        print("Your score is now " + str(score))
    print('Success! Total score: ' + str(score))
