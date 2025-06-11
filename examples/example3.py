class DB:
    def __init__(self) -> None:
        self.data = {}

    def add_user(self, user_id: int, name: str) -> None:
        if type(user_id) is not int:
            raise TypeError("User id must be integer")
        if user_id in self.data:
            raise ValueError("User already exists")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        self.data[user_id] = name

    def get_user(self, user_id: int) -> str:
        if user_id not in self.data:
            raise ValueError("User not found")
        return self.data[user_id]

    def delete_user(self, user_id: int) -> None:
        if user_id not in self.data:
            raise ValueError("User not found")
        del self.data[user_id]
