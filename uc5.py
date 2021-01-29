import csv

# indian state names with its population and rank based on area
indian_state_profiles = [
    {'name': 'Andra Pradesh', 'population': 49506799, 'area rank': 7},
    {'name': 'Arunachal Pradesh', 'population': 1383727, 'area rank': 14},
    {'name': 'Assam', 'population': 31205576, 'area rank': 16},
    {'name': 'Bihar', 'population': 104099452, 'area rank': 12},
    {'name': 'Chhattisgarh', 'population': 25545198, 'area rank': 9},
    {'name': 'Goa', 'population': 1458545, 'area rank': 28},
    {'name': 'Gujarat', 'population': 60439692, 'area rank': 5},
    {'name': 'Haryana', 'population': 25351462, 'area rank': 20},
    {'name': 'Himachal Pradesh', 'population': 6864602, 'area rank': 17},
    {'name': 'Jharkhand', 'population': 32988134, 'area rank': 15},
    {'name': 'Karnataka', 'population': 61095297, 'area rank': 6},
    {'name': 'Kerala', 'population': 33406061, 'area rank': 21},
    {'name': 'Madhya Pradesh', 'population': 72626809, 'area rank': 2},
    {'name': 'Maharashtra', 'population': 112374333, 'area rank': 3},
    {'name': 'Manipur', 'population': 2855794, 'area rank': 23},
    {'name': 'Meghalaya', 'population': 2966889, 'area rank': 22},
    {'name': 'Mizoram', 'population': 1097206, 'area rank': 24},
    {'name': 'Nagaland', 'population': 1978502, 'area rank': 25},
    {'name': 'Odisha', 'population': 41974218, 'area rank': 8},
    {'name': 'Punjab', 'population': 27743338, 'area rank': 19},
    {'name': 'Rajasthan', 'population': 68548437, 'area rank': 1},
    {'name': 'Sikkim', 'population': 610577, 'area rank': 27},
    {'name': 'Tamil Nadu', 'population': 72147030, 'area rank': 10},
    {'name': 'Telangana', 'population': 35193978, 'area rank': 11},
    {'name': 'Tripura', 'population': 3673917, 'area rank': 26},
    {'name': 'Uttar Pradesh', 'population': 199812341, 'area rank': 4},
    {'name': 'Uttarakhand', 'population': 10086292, 'area rank': 18},
    {'name': 'West Bengal', 'population': 91276115, 'area rank': 13},
]

# display the details of indian_state_profile
print('Name, Population, Area Rank')
for state in indian_state_profiles:
    print([atr for atr in state.values()])

# column header
fields = ['name', 'population', 'area rank']

# writing to csv file
with open('Indian_state_list.csv', 'w', newline='') as fileObj:

    # object to write indian_state_profile to csv file
    csvObj = csv.DictWriter(fileObj, fieldnames=fields)

    # writing header of the column
    csvObj.writeheader()

    # writing the data of indian_state_profile to file
    csvObj.writerows(indian_state_profiles)
