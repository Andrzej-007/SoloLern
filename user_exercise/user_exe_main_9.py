

class User():

    def __init__(self, first_n, last_n,age, email ):
        self.first_name = first_n
        self.last_name = last_n
        self.age = age
        self.email = email

    def describe_user(self):
        print(f'the user name: {self.first_name.title()}')
        print(f"the surname: {self.last_name.title()}")
        print(f"age:{ self.age}")
        print(f"email: {self.email}")


    def greet_user(self):

        print(f"\nDear user Wellcome again {self.first_name.title()} {self.last_name.title()}")




# user_and = User('andrzej', 'kozlowski', 47, 'and@emial')
# user_and.describe_user()
# user_and.greet_user()
#
# entitelment_list = ['can add post', 'can edit post', 'can remove post']
# admin = Admin('andrzej', 'kozlowski')

# admin.describe_user()
# admin.privileges.admin_privilages = entitelment_list
# admin.greet_user()
# admin.privileges.show_privileges()