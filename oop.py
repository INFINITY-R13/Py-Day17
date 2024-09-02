class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        
user1 = User(101, 'infinity')

print(user1.id)
print(user1.username)
print(user1.follower)

