name = "this is a book"

split_name = name.split() # by default -> split on space
print(split_name) # ['this', 'is', 'a', 'book']

join_name = "-".join(split_name)
print(join_name) # this is a book
