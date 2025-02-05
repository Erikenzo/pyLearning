fileName = input("Please enter your file name: ")

if fileName.lower().endswith(".gif"):
    print("image/gif")
elif fileName.lower().endswith(".jpeg"):
    print("	image/jpeg")
else:
    print("other file category")

### not adding all of the file endings since without placing it in to list I will just simply write same elif x6 more times.
