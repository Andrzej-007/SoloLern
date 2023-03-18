

file_path = '../text_folder/alice.txt'

with open (file_path) as file_object:
    content = file_object.read()

num_of_words = content.lower().count('the')
print(f' number of the in file equols {num_of_words}\n')

words_dictionary ={}
list_of_words = content.split()
print(f'list_of_words\n')

for i in list_of_words:
    x = i.lower()
    if x in words_dictionary:
        words_dictionary[x] += 1
    else:
        words_dictionary[x] = 1

# print(f'\nthe number of perticular worgs are as follows : {words_dictionary} ')

list_max_words = list()
for key, value in words_dictionary.items():
    if value > 100:
        a = (key,value)
        list_max_words.append(a)

print(f'max words {list_max_words}')
