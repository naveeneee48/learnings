import subprocess

# command = subprocess.run(['df','-h'],capture_output=True,text=True)
# print(command.stdout)

# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_set = set(my_list)
# print(unique_set)
def remove_duplicate(input_value):
    # unique_set = sorted(set(input_value))
    # sorted_set = sorted(input_value)
    input_value.sort(reverse=True)  
    return input_value
print(remove_duplicate([1,6,2,3,3,4]))


#list
# myfile = [13,5,2,4]
# command = len(myfile)
# total = sum(myfile)
# total = max(myfile)
# total = min(myfile)
# total = sorted(myfile)


listed_file = [1,2,3,3]
print(set(listed_file))
