class User:
    def __init__(self, user_name, id_number):
        print('User had been created...')
        self.name = user_name
        self.id_number = id_number
        self.followers = 0 # default value


user_1 = User("Angela", "001")
print(f'user name: {user_1.name}, id {user_1.id_number} and number of followers {user_1.followers}')
user_2 = User("Bob", "002")
print(user_2.name,  user_1.id_number)