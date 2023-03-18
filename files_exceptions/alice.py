

file_path = '../text_folder/alice.txt'


def count_number_of_words(path):

    file_path = f'../text_folder/{path}'
    try:
        with open(file_path) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        message = f'\nfile name {file_path} does not exist'
        print(message)

    else:
        words = content.split()
        count_words = len(words)
        print(f'\n text from file {file_path} contain {count_words} number of words')


list_of_files = ['alice.txt', 'hello_its_me.txt','we_dont_have','learning_python.txt' ]

for file in list_of_files:
    count_number_of_words(file)

