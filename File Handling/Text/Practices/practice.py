path = "File Handling/Text/Practices/contentx.txt"

f = open(path, 'rt')
contents = f.read()
f.close()

contents = contents.upper()

f = open(path, "wt")
f.write(contents)
f.close()
