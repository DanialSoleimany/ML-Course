import json 

path = "File Handling/Json/Dump/contents.json"
contents = {}

with open(path, 'w') as f:
    json.dump(contents, f, indent=4)