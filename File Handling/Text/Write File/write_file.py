path = "File Handling/Text/Write File/contents.txt"

f = open(path, 'w')
contents = f.write("hello world")
f.close()
