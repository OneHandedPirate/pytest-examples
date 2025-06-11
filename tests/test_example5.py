import pytest
from examples.example5 import get_weather


@pytest.fixture
def city() -> str:
    return "London"


@pytest.fixture
def api_key() -> str:
    return "valid_api_key"


@pytest.fixture
def invalid_api_key() -> str:
    return "Invalid_api_key"


def test_get_weather_success(mocker, city, api_key):
    mock_get = mocker.patch("examples.example5.requests.get")

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"main": {"temp": 293.15}}
    mock_get.return_value = mock_response

    temperature = get_weather(city, api_key)

    mock_get.assert_called_once_with(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    )
    assert temperature == 20.0


def test_get_weather_invalid_api_key(mocker, city, invalid_api_key):
    mock_get = mocker.patch("examples.example5.requests.get")
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_get.return_value = mock_response

    with pytest.raises(ValueError, match="Invalid API key"):
        get_weather(city, invalid_api_key)

    mock_get.assert_called_once_with(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={invalid_api_key}"
    )


def test_get_weather_other_error(mocker, city, api_key):
    mock_get = mocker.patch("examples.example5.requests.get")
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    with pytest.raises(ValueError, match="Couldn't get weather data"):
        get_weather(city, api_key)

    mock_get.assert_called_once_with(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    )


def test_get_weather_no_temp_data(mocker, city, api_key):
    mock_get = mocker.patch("examples.example5.requests.get")
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"some_other_data": "value"}
    mock_get.return_value = mock_response

    temperature = get_weather(city, api_key)

    assert temperature is None
    mock_get.assert_called_once_with(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    )


def test_get_weather_invalid_city_type(api_key):
    with pytest.raises(TypeError, match="City must be a string"):
        get_weather(123, api_key)


def test_get_weather_invalid_api_key_type(city):
    with pytest.raises(TypeError, match="API key must be a string"):
        get_weather(city, 123)
