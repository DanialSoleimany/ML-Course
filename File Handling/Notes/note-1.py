path = "File Handling/Notes/content.txt"

f = open(path, 'r')
contents = f.read()
f.close()

print(contents)

# same as 

with open(path, "r") as f:
    contents = f.read()

print(contents)