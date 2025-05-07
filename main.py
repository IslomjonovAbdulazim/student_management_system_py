from models.user import User

User.create_table()
user = User("admin-2", "qwerty", "admin", 10)
user.save()
print(user.get_all()[2].print_info())


