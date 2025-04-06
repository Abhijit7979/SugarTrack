from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Simple in-memory database for users
users_db = {}

class User(UserMixin):
    def __init__(self, id, username, email, password_hash, coin_balance=0, daily_goal_minutes=120, streak_count=0, today_progress=0):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.coin_balance = coin_balance
        self.daily_goal_minutes = daily_goal_minutes
        self.streak_count = streak_count
        self.today_progress = today_progress

    @staticmethod
    def get(user_id):
        # Get user from our in-memory database
        return users_db.get(user_id)
    
    @staticmethod
    def get_by_email(email):
        # Find user by email
        for user in users_db.values():
            if user.email == email:
                return user
        return None
    
    @staticmethod
    def create(username, email, password, daily_goal_minutes=120):
        # Create a new user
        user_id = str(len(users_db) + 1)  # Simple ID generation
        password_hash = generate_password_hash(password)
        
        new_user = User(
            id=user_id,
            username=username,
            email=email,
            password_hash=password_hash,
            daily_goal_minutes=daily_goal_minutes
        )
        
        users_db[user_id] = new_user
        return new_user
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Initialize with a test user
if not users_db:
    test_user = User(
        id="1",
        username="TestUser",
        email="test@example.com",
        password_hash=generate_password_hash("password123"),
        coin_balance=75,
        daily_goal_minutes=120,
        streak_count=5,
        today_progress=45
    )
    users_db["1"] = test_user 