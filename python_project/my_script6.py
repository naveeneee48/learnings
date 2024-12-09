import  requests

#call the api and get the json file and convert json to python readable dict format
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(response.json())
# print(response.status_code)
complete_details = response.json()
#.json() will convert json file into List
# print(complete_details)
for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])
    ############
