class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

        
user1 = User(101, 'infinity')
user2 = User(000, 'zero')

user1.follow(user2)

print(user1.id)
print(user1.username)
print(user1.followers)

print("\n")

print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)

