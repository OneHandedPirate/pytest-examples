import pytest

from examples.example1 import get_weather


def test_get_weather():
    assert get_weather(31) == "hot"
    assert get_weather(3) == "cold"
    with pytest.raises(TypeError, match="Temperature must be an integer"):
        get_weather("Not a valid input")
