# creating a file object for file operations
fileObj = open('name_list.txt', 'r')

# reading data from the file and adding it to a list
name_list = [name for name in fileObj.read().split('\n')]

# display the items in names_list
for name in name_list:
    print(name)
