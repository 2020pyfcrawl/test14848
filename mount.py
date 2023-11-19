#!/usr/bin/env python3

import subprocess


def is_nfs_mounted(mount_point):
    if len(mount_point) == 0:
    	return False
    try:
        # use mount to check
        process = subprocess.run('mount | grep nfs', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        mount_point = ' ' + mount_point + ' '
        if mount_point in process.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False

def mount_detail_check(port, protocol):
    if len(port) == 0 | len(protocol) == 0:
        return False
    try:
        process = subprocess.run('mount | grep nfs', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        port = "mountport=" + port
        protocol = "mountproto=" + protocol
        if (port in process.stdout) & (protocol in process.stdout):
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False



def is_nfs_unmounted():
    try:
        process = subprocess.run('mount | grep nfs', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        if process.stdout:
            print("NFS mount still existed")
            return False;
        else:
            return True;
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False


