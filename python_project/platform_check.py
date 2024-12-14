import platform
import os
# def sys():
#     if platform.system() == 'Linux':
#         print("Linux OS Detected")

#     elif platform.system() == 'Windows' or 'MINGW' or 'CYGWI':
#         print("Windows OS Detected")

# sys()

# def sys2():
#     if platform.system() == "Linux":
#         print("Linux os Detected==========")
#     elif platform.system() == "Windows":
#         print("Windows os detected")
# sys2()

# my_file = "sample.py"

# if os.path.exists(my_file):
#     print(f"file {my_file} exist")
# else:
#     print(f"file {my_file} not exist")

# my_file2 = "sample.txt"
# if os.path.exists(my_file2):
#     os.remove(my_file2)             
#     print(f"file {my_file2} deleted")
# else:
#     print(f"file {my_file2} not deleted")
# import subprocess

# command = "sudo systemctl status openvpn.service"
# output = subprocess.run(command, shell=True, text=True)
# print(output)

# lines_to_add = "hello world!!"
# with open("example.txt","w") as text_file:
#     text_file.write(lines_to_add)

# print(f"the content {lines_to_add} added")

# lines_to_add = "hello world!!"
# with open("example.txt", "w") as text_file:
#     text_file.write(lines_to_add)

# print(f"The content {lines_to_add} added")

# with open("example.txt", "r") as read_file:
#     content = read_file.read()

# print(content)

# file_content = "hello hariish!!"
# with open("example.txt" ,"a") as append_file:
#     append_file.write(file_content + "\n")
# print(f"content of {file_content} appended")

# import subprocess


# command = subprocess.run(["df","-h"])
# print(command)

# with open("example.txt","r") as output_file:
#     try:
#      content = output_file.read()
#      print(content)
#     except:
#      print("content not executed properly")

# dir = "/home/naveen/naveenkumar"
# # command = os.mkdir(dir)
# if os.path.exists(dir):
#     print(f"folder {dir} exist")
# else:
#     print(f"folder {dir} not exist")

# command = os.system("df -h")
# print(command)

# cores = os.cpu_count()
# print(cores)
# import requests

# url = "https://jsonplaceholder.typicode.com/posts/"
# response = requests.get(url)

# # if response.status_code == 200:
# #     print(f"success with status code of {response.status_code}")

# data = {
#     "name": "naveen"
# }
# response2 = requests.post(url,json=data)
# print(response2.status_code)
import paramiko

# ssh_client = paramiko.SSHClient()
# # Automatically add the server's host key if it's not already known
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # Establish the connection
# print("Connecting to the server...")
# ssh_client.connect("10.4.0.38", port=22, username="naveen", password="naveen")
# print("Connected!")


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
ssh_client.connect("10.12.0.100",port=22,username="<username>",password="<password>")
print("server connected")
command = "hostnamectl"
stdin, stdout, stderr = ssh_client.exec_command(command)
print(stdout.read().decode())
# ssh_client.close()
# print("connection closed")

sftp = ssh_client.open_sftp()
sftp.put("local_file.txt", "remote_file.txt")
sftp.get("remote_file.txt","local_file.txt")
