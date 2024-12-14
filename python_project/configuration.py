import json

# with open("config.json","r") as file:
#     data = json.load(file)
# print(data)

# write_data = {
#     "name": "hariish"
# }
# with open("conf.json","w") as file2:
#    json.dump(write_data,file2,indent=4)

# # input_file = "hello this is naveen!!!"

# with open("hello.txt","r") as file3:
# #    json.dump(write_data,file2,indent=4)
#     #   file2.write(input_file)
#      content =  file3.read()
# print(content)


# with open("config.json","r") as file:
#     data = json.load(file)
# print(data)


write_file = "sample text file edit !!!"
with open("hello.txt","w") as written_file:
    written_file.write(write_file)