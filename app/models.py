from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, email, coin_balance=0, daily_goal_minutes=120, streak_count=0, today_progress=0):
        self.id = id
        self.username = username
        self.email = email
        self.coin_balance = coin_balance
        self.daily_goal_minutes = daily_goal_minutes
        self.streak_count = streak_count
        self.today_progress = today_progress

    @staticmethod
    def get(user_id):
        # For the prototype, we'll just use a hardcoded user
        # In a real application, this would fetch the user from the database
        if user_id == "1":
            return User(
                id="1",
                username="TestUser",
                email="test@example.com",
                coin_balance=75,
                daily_goal_minutes=120,
                streak_count=5,
                today_progress=45
            )
        return None 