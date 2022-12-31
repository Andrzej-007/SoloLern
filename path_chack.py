import os

t = os.path.join('Users' ,'andrzej_kozlowski', 'PycharmProjects', 'SoloLern')
print(t)


with open('text_folder/hello_its_me.txt') as my_file:
    content = my_file.read()
    print(content.rstrip())   # rstrip() - to avaoid the blank line at the end of the line

print('********')

# example OS X : '/home/ehmatthes/other_files/text_files/filename.txt'
# exmaple Windows : file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'

file_patch = '/Users/andrzej_kozlowski/my_text_file.txt'
with open (file_patch) as object_two:
    # content_two = object_two.read()
    # print(content_two)

    for easch_line in object_two:
        print(easch_line)
