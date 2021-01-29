# list having names of people
name_list = [
    'Aashrith', 'Badri', 'Gayathri',
    'Kiran', 'Omesh', 'Rakesh',
    'Sabari', 'Vamsi'
]

# display the items in name_list
for name in name_list:
    print(name)

# adding items to name_list
name_list.append('John')
print('list after adding name : ', name_list)

# removing items from name_list
name_list.remove('Kiran')
print('list after deleting name : ', name_list)
