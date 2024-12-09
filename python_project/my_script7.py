#understand what is file operations
#when you want to update/read or delete a file, we need file operations concept
#regular case for automation is python because we can run it in windows also
def update_server_conf(file_path,key,value):
    with open(file_path,"r") as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key+ "=" + value + "\n" )
            else:
                file.write(line)

update_server_conf("server.conf","MAX_CONNECTIONS","1000")


# with open("touch.txt", "r") as file:
#     content = file.read()
#     print(content)

import os

# move_file = os.rename("naveen.txt","ravina.txt")
change_mode=os.chmod("ravina.txt", +x)
