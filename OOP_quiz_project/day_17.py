class User:
    def __init__(self, id, username):
        print("New user being reated...")
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1





user_1 = User("001", "MIke")
user_2 = User("001", "angela")

user_1.follow(user_2)

# print(user_1.username)
# print(user_1.id)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)


