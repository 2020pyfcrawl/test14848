#!/usr/bin/env python3

import subprocess

def is_existed():
    try:
        process = subprocess.run(['ls /home/student/Desktop '], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if 'HowtoReadPaper.pdf' in process.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False
    
def is_existed_1():
    try:
        process = subprocess.run(['ls -al /home/student/Desktop HowtoReadPaper.pdf'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)       
        if ('HowtoReadPaper.pdf' in process.stdout) & ('74475' in process.stdout):
            return True 
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False

        
def is_nfs_existed():
    try:
        process = subprocess.run(['ls /home/student/Desktop/nfstemp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if 'test' in process.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False

def is_tartans_existed():
    try:
        process = subprocess.run(['ls /home/student/Desktop/nfstemp '], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if 'test' in process.stdout and 'tartans@1' in process.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False
