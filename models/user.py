# Create user class

class User:
    def __init__(self, username, full_name, email=None):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.user_id = str(uuid.uuid4())  # generates a unique user ID

    def __str__(self):
        return f"{self.full_name} ({self.username})"