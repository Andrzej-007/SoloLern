
from user_exe_main_9 import User


class Admin(User):

    def __init__(self,first_n, last_n,age="None", email='admin@admoin.net' ):
        super().__init__(first_n, last_n,age, email)
        self.privileges = Privileges()


class Privileges():

    def __init__(self):
        self.admin_privilages = []

    def show_privileges(self):
        print(f"\nbelow the following admin's authorities: ")
        for i in self.admin_privilages:
            print(f'-{i}')
