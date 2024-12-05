import json 

path = "File Handling/Json/Practices/contents.json"

with open(path, 'r') as f:
    contents = json.load(f)

contents["age"] = 23 # -> {"age":23}

with open(path, 'w') as f:
    json.dump(contents, f, indent=4)