# Creating classes

class User:
    print("New user being created...")
    def __init__(self, user_id, first_name, last_name):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Fred", "Sheehan")
user_2 = User("002", "John", "Doe")

user_1.follow(user_2)

print(
    user_1.id, user_1.first_name, user_1.last_name,
    user_1.followers, user_1.following,
)

print(
    user_2.id, user_2.first_name, user_2.last_name,
    user_2.followers, user_2.following,
)
