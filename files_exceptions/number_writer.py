

import json

numbers = [1,3,5,7,9,11,13]

''' as we want to seve file in diffrent location'''
# file_name = '../text_folder/numbers_json'
file_name = 'numbers.json'

# with open (file_name, 'w') as file_obect:
#     json.dump(numbers, file_obect)

with open (file_name) as file_object:
    content = json.load(file_object)

print(content)