import requests


def get_weather(city: str, api_key: str):
    if not isinstance(city, str):
        raise TypeError("City must be a string")

    if not isinstance(api_key, str):
        raise TypeError("API key must be a string")

    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    )

    status_code = resp.status_code

    if status_code == 401:
        raise ValueError("Invalid API key")
    elif status_code != 200:
        raise ValueError("Couldn't get weather data")

    current_temp = resp.json().get("main", {}).get("temp", 0)
    return round(current_temp - 273.15, 3) if current_temp else None
