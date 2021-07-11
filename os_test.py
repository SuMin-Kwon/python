import os
print(os.getcwd())
print(os.listdir())
os.mkdir("새폴더2")

with os.scandir("C:/Python work/1일차") as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():   
            print(entry.name)