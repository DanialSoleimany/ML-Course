path = "File Handling/Text/Read File/contents.txt"

f = open(path, 'rt')
contents = f.read()
f.close()

print(contents)
