#if you want to do a repetitive of action , thn we will use loops
#for varibale in sequence(range/list/tuple)

# for i in range(10):
#     print(i)
#     print("naveen")

colors=["red","yellow","green"]
for i in colors:
    print(i)

# List of services to monitor
services = ["nginx", "mysql", "redis"]
index = 0

for service in services:
    print(f"list of services are {service}")
#This line uses an f-string (formatted string literal) to insert the value of service into the string.

while index < len (services):
    print(f"Checking status of {services[index]}...")
    # Add service status check logic
    index += 1

numbers= [1,2,3,4]
for number in numbers:
    if number == numbers[2]:
        break #it will display the statement untill number[2]
    print(number)

for number in numbers:
    if number == numbers[2]:
        continue #it will skip the particular condition  number[2]
    print(number)
    
#take values from real-time 
# numbers = input("provide your beautiful name:")
# print(f"hai {numbers} !! how are you ?? !!!!")

# folders = input("provide folder details:").split()
# print(folders)
#o/p 
# provide folder details:/opt /etc
# ['/opt', '/etc']
folders = input("provide folder details:").split()
for folder in  folders:
    print(folder)