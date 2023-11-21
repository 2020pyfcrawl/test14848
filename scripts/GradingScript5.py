import subprocess

# Server details
hostname = "1.2.3.4"
username = "student"
directory = "/home/student/mnt/important"

# SSH command to check if directory exists
check_command = f'ssh {username}@{hostname} "test -d \\"{directory}\\" && echo Exists || echo Does not exist"'

# Execute the command and capture the output
try:
    result = subprocess.run(check_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout.strip()

    # Check output and print result
    if output == "Exists":
        print("Pass")
    else:
        print("Fail")
except subprocess.CalledProcessError as e:
    print("Failed to execute command:", e)

