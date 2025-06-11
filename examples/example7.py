import requests


class ApiClient:
    @staticmethod
    def get_user_data(user_id: int) -> dict:
        resp = requests.get(f"https://api.example.com/users/{user_id}")

        if resp.status_code != 200:
            raise ValueError("Api request failed")

        return resp.json()


class UserService:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def get_username(self, user_id: int) -> str:
        if type(user_id) is not int:
            raise TypeError("User id must be an integer")

        user_data = self.api_client.get_user_data(user_id)

        return user_data["username"].upper()
