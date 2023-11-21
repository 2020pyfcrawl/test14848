from truenas_checker import check_truenas_dataset_and_smb_access

# Usage of the function with credentials and parameters, you can use other username/password and dataset for testing
dataset_name = 'photos/cmu'  # Dataset path/name
username = 'samba'  # SMB Username
password = 'samba'  # SMB Password

# Call the function
status, space, smb_details = check_truenas_dataset_and_smb_access(dataset_name, username, password)
if status:
    print("Grading script 1 check: Passed!")
else:
    print("Grading script 1 check: Failed!")

# Other information that can also be used for checking
# if smb_details:
#     print(f"Available space: {space}")
#     print(f"SMB Share '{smb_details['name']}' details:")
#     print(f"  Path: {smb_details['path']}")
#     print(f"  Description: {smb_details['comment']}")
