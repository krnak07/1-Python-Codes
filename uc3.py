# list having names of people
name_list = [
    'Aashrith', 'Badri', 'Gayathri',
    'Kiran', 'Omesh', 'Rakesh',
    'Sabari', 'Vamsi'
]

# creating a file object for file operations
fileObj = open('name_list.txt', 'w')

# write the items in the name_list to the file
for name in name_list:
    fileObj.write(name+'\n')

# closing the file
fileObj.close()
