def get_weather(temp: int) -> str:
    if not isinstance(temp, int):
        raise TypeError("Temperature must be an integer")
    if temp < 30:
        return "cold"
    else:
        return "hot"
