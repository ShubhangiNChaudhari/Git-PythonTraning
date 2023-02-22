class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


class UserAPI:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)

    def get_users(self):
        user_list = []
        for user in self.users:
            user_list.append({"name": user.get_name(), "email": user.get_email()})
        return user_list


api = UserAPI()
api.add_user("John Doe", "john.doe@example.com")
api.add_user("Jane Smith", "jane.smith@example.com")

users = api.get_users()
for user in users:
    print(user["name"], user["email"])
