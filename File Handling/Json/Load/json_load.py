import json 

path = "File Handling/Json/Load/contents.json"

with open(path, 'r') as f:
    contents = json.load(f)

print(contents)