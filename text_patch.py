

file_patch = '/Users/andrzej_kozlowski/my_text_secend.txt'
file_patch_01 = '../../my_text_secend.txt'

# "../../my_text_file.txt"
# /Users/andrzej_kozlowski/my_text_secend.txt
# /Users/andrzej_kozlowski/PycharmProjects/SoloLern/text_patch.py

with open (file_patch_01, mode='a') as file_obect:
    content = file_obect.write('new line to write 11 as a amendment\n')
    # content = file_obect.write('\n new line to write 09')

    # content = file_obect.read()
    # print(content)

print('******* new_task ')
user_name_path = 'text_folder/user_name.txt'
number_of_users = 0
while True:
    number_of_users += 1
    user_name = input(f'{number_of_users} please write down your name or type q to exit:..\n' )
    if user_name.lower() == 'q':
        break
    else:
        with open (user_name_path, mode='a') as user_location:
            content = user_location.write(f'{user_name}\n')
