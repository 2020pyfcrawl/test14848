# test14848

mount.py
#!/usr/bin/env python3

import subprocess

# NFS挂载点路径
nfs_mount_point = "/your/nfs/mount/point"

def is_nfs_mounted(mount_point):
    try:
        # 执行 mount 命令并通过 grep 检索 NFS 挂载
        process = subprocess.run('mount | grep nfs', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        # 检查输出中是否有指定的挂载点
        if mount_point in process.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False


def is_nfs_unmounted():
    try:
        # 执行 mount 命令并通过 grep 检索 NFS 挂载
        process = subprocess.run('mount | grep nfs', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        if process.stdout:
            # 有输出
            print("NFS mount still existed")
            #print(process.stdout)
            return False;
        else:
            return True;
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False


ls.py
#!/usr/bin/env python3

import subprocess

def is_existed():
    try:
        process = subprocess.run(['ls ~/Desktop/14761 main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        # 检查输出中是否有指定的挂载点
        if 'main.py' in process.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False
