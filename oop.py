# Defines the blueprint for creating user objects.
class User:
    # The __init__ method is the constructor. It's called automatically
    # whenever a new User object is created.
    def __init__(self, user_id, username):
        """
        Initializes a new User instance.
        """
        # --- Attributes ---
        # 'self' refers to the object being created.
        self.id = user_id          # Assigns the provided user_id to the object.
        self.username = username   # Assigns the provided username to the object.
        self.followers = 0         # Initializes followers count to 0 for a new user.
        self.following = 0         # Initializes following count to 0 for a new user.

    # Defines a method (an action the object can perform).
    def follow(self, user_to_follow):
        """
        Makes the current user ('self') follow another user ('user_to_follow').
        """
        # The user doing the action increases their 'following' count.
        self.following += 1
        # The user being followed gets a new follower.
        user_to_follow.followers += 1


# --- Program Execution ---

# Create an instance (object) of the User class.
user1 = User(101, 'infinity')

# Create a second instance of the User class.
# The user_id is 0. Using '000' would cause a SyntaxError.
user2 = User(0, 'zero')

# user1 calls the follow() method on user2.
# 'self' inside the method is user1.
# 'user_to_follow' inside the method is user2.
user1.follow(user2)

# --- Output ---

# Print attributes of user1
print(f"User 1 ID: {user1.id}")
print(f"User 1 Username: {user1.username}")

print("\n--- Social Stats ---")

# After user1 followed user2:
# user1's following count is now 1.
print(f"User 1 is following: {user1.following}")
# user1's followers count is still 0.
print(f"User 1 has followers: {user1.followers}")

# user2's following count is still 0.
print(f"User 2 is following: {user2.following}")
# user2's followers count is now 1.
print(f"User 2 has followers: {user2.followers}")