import os
#learn try and exception handling

folders = input("provide folder details:").split()
# folders = ['/opt','/xyz','/fve']
for folder in  folders:
    try:
        files = os.listdir(folder)
        print("listing the files in " +folder+" below")
    except FileNotFoundError:
        print("provide correct folder name")
        break 
    except PermissionError:
        print("permission error to this folder" + folder)
    print(files)
    for file in files:
        print(f"the file is {file}")
    
