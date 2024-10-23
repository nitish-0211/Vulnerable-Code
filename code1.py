import os
import subprocess

# Hardcoded secret (bad practice)
SECRET_KEY = "hardcoded_secret"

# Using eval (dangerous, can lead to code injection)
user_input = input("Enter some Python code to evaluate: ")
eval(user_input)

# Using subprocess with shell=True (potential command injection vulnerability)
def run_system_command(cmd):
    subprocess.run(cmd, shell=True)

run_system_command("ls -l")

# Weak hashing algorithm (MD5 is insecure)
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

password = "user_password"
print(hash_password(password))
