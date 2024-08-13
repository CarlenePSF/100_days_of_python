class User:
    def __init__(self, user_name, id_number):
        print('User had been created...')
        self.name = user_name
        self.id_number = id_number
        self.followers = 0 # default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("Angela", "001")
user_2 = User("Bob", "002")

print(f'user name: {user_1.name},'
      f'id {user_1.id_number},'
      f' number of followers {user_1.followers}'
      f' and following {user_1.following}')

# call a method
user_1.follow(user_2)

print(f'user name: {user_1.name},'
      f'id {user_1.id_number},'
      f' number of followers {user_1.followers}'
      f' and following {user_1.following}')
