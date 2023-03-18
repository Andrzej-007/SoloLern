

from admin_privilages import Admin, Privileges
from user_exe_main_9 import User


mp_admin = Admin('kuba', 'golec', 48)
mp_admin.describe_user()

entitelment_list = ['can add post', 'can edit post', 'can remove post']
mp_admin.privileges.admin_privilages = entitelment_list
mp_admin.privileges.show_privileges()

