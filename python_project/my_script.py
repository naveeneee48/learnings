
import sys
import os

x = 1 #whole number
y = 1.5   #decimal number
z = "strilg file" #string
is_true = True #boolean
print(x)
print(y)
print(z)
print(is_true)
#=================
age = 15
if age >= 18:
    print("you are a minor")
else:
    print("you are a major")
#===========
for i in range(5):
    print(i)
#=================
count = 0
while count < 5:
     print(count)
     count += 1
age = 17
if age >= 18:
    print("you can vote")
else:
    print("you can not vote")
#===============
age = 18
if age >= 18:
    print("you are adult")
elif age >= 13:
    print("you are a teenage")
else:
    print("all are good")
#=================
txt = "Naveen kumar"
txt2 = "good boy"
result = txt+txt2
print(result)
#==============
file = 3.5734343
print(round(file))
###################
file = "rfhigvndoinvwr"
print(len(file))
print(file.upper())
print(file.lower())
#############33333333333
#function
#adv = readability of the code ,reusability and debugging

def addition(num1,num2):
    add=num1+num2
    print(add)

def substraction(num1,num2):
    sub=num1-num2
    print(sub)

def addition2(num1,num2):
    sum = num1 * num2
    return sum

#we have to pass the argument as "python3 my_script.py 2 3"
#for this work we have to do "import sys"
num1=int(sys.argv[1])
num2=int(sys.argv[2])
operation=sys.argv[3]
print("function value is for addition and subtraction")
# substraction()
# print(addition())
# print(addition2(num1,num2))
############################
 
if operation == "add":
    result = addition2(num1,num2)
    print(result)

if operation == "sub":
    result2 = substraction(num1,num2)
    print(result2)

password=os.getenv("password")
print(password)


##operators
#assignment operator
a = 2
a += 2 # neaning is 'a = a+2'
print(a)

#boolean data type
#identity operator
a = 5
b = 5
note1 = a is b
note2 = a is not b
print(note1)
print(note2)

x = True
y = False
result = x and y
print(result)
# result will be False

#logical operator
a = True
b = False
result = a or b
print(result)
# result will be True


 