from typing import Optional


class UserManager:
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, username: str = None, email: str = None) -> None:
        if not isinstance(username, str) or not isinstance(email, str):
            raise TypeError("Username and email must be strings")
        if username in self.users:
            raise ValueError(f"User {username} already registered")
        self.users[username] = email

    def get_user(self, username: str = None) -> dict[str, str]:
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        user_email: Optional[str] = self.users.get(username)
        if user_email is None:
            raise ValueError("User not found")
        return {
            "username": username,
            "email": user_email,
        }

    def get_users(self) -> dict[str, str]:
        return self.users
