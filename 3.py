#!/usr/bin/env python
import mount
import ls
import hashlib


def get_input(prompt):
    return input(prompt)

questions = [
    "Q1: check mount",
    "Q2: check file",
    "Q3: How many files in the dataset you mount in total? (not including folders)",
    "Q4: Find out which port and protocol you use when use command mount before. (Format:8888:TCP) ",
    "Q5: Check umount"
]

# The hashes here are placeholders and should be replaced with the SHA256 hashes
# of the correct answers to the questions for the TrueNAS challenge
answers = [
    '0',  
    '1', 
    '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', 
    '5',
    '6'
]

scores = [
    20,20,20,20,20
]

def recursively_prompt_question(index, expected_hash):
    if index == 0:
        print("Q1: We will check if you have already mount the NFS")
        user_input = get_input("Please input your local mount path (full/absolute path name)" + '\n> ').strip()
        return mount.is_nfs_mounted(user_input)
        
    elif index == 1:
        print("Q2: We will check if you have already put the paper mentioned before to the Desktop.")
        user_input = get_input("Please press Enter to continue" + '\n> ').strip()
        #...check with ls
        return ls.is_existed_1()
        
    elif index == 2:
        user_input = get_input(questions[index] + '\n> ').strip()
        if hashlib.sha256(user_input.encode()).hexdigest() == expected_hash:
            # print("Correct! ... +20 points\n")
            return True
        else:
            print("Incorrect. Let's try again!\n")
            return False

    elif index == 3:
        user_input = get_input("Q6: Find out which port and protocol you use when use command mount before. (Format:8888:TCP)" + '\n> ').strip();
        parts = user_input.lower().split(':')        
        return mount.mount_detail_check(parts[0],parts[1])

    elif index == 4:
        print("Q7: Now exit all mounted files, and umount the dataset from your computer using command `umount {mounted_file_path}`.")
        user_input = get_input("Please press Enter to continue, then we will check if you have successfully unmount." + '\n> ').strip()
        return mount.is_nfs_unmounted()
    else:
        print("ERROR")
        return False

if __name__ == "__main__":
    score = 0
    for i in range(0,len(questions)):
        result = False
        while recursively_prompt_question(i, answers[i]) == False:
            print("Wrong Answer!")
        print("Correct Answer!")
        score += scores[i]
        print("Your score is now " + str(score))
    print('Success! Total score: ' + str(score))
