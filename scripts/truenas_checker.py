import requests

BASE_URL = 'http://truenas.aia'

def check_dataset_existence_and_space(dataset_name, username, password):
    # Start a session for API calls
    session = requests.Session()
    session.auth = (username, password)

    try:
        response = session.get(f'{BASE_URL}/api/v2.0/pool/dataset')
        response.raise_for_status()
        datasets = response.json()
        for dataset in datasets:
            if dataset_name in dataset['name']:
                available_space = dataset['available']['rawvalue']
                return True, available_space
        return False, None
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return False, None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return False, None

def check_smb_access(dataset_name, username, password):
    session = requests.Session()
    session.auth = (username, password)
    try:
        response = session.get(f'{BASE_URL}/api/v2.0/sharing/smb/')
        response.raise_for_status()
        smb_shares = response.json()
        for share in smb_shares:
            if dataset_name in share['path']:
                if share.get('guestok') is False and share.get('browsable') is True:
                    return share
        return None
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None


def check_truenas_dataset_and_smb_access(dataset_name, username, password):

    # Check the dataset existence and available space
    dataset_exists, available_space = check_dataset_existence_and_space(dataset_name, username, password)
    # Check the SMB access
    smb_access = check_smb_access(dataset_name, username, password)

    # Combine the checks for final status
    if dataset_exists and smb_access:
        return True, available_space, smb_access
    else:
        return False, available_space, smb_access

