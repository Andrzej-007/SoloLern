import json


# user_file = f'{user_imput}.json'
# user_imput = input('what you user name :..')
#
# with open(user_file, 'w') as f_object:
#     json.dump(user_imput,f_object)
#     print(f'we will remember when your come back {user_imput}')
#
# user_path = 'tonkiel.json'
# with open(user_path) as f_object:
#     username = json.load(f_object)
#     print(f'welcome beck username : {username}')




def great_ueser():
     
     file_user = 'username.json'
     try:
         with open(file_user) as f_object:
             username = json.load(f_object)

     except FileNotFoundError:
         username = input(f'your are the first time please type your username')
         with open(file_user, 'w') as f_object:
             json.dump(username, f_object)
             print(f'welcome new {username}')
     else:
         print(f'wellcome back {username} ')


great_ueser()