from user import User
from admin import Admin

new_user = User('Dongmin', 'Seo', 21, 169, 74)
admin = Admin("Secret", 'Agent', 50, 50, 50)
print(admin.privileges.show_privileges())