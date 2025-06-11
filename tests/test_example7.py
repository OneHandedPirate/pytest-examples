import pytest

from examples.example7 import ApiClient, UserService

@pytest.fixture
def user_id() -> int:
    return 1

@pytest.fixture
def username() -> str:
    return "Dmitry"


def test_get_username_with_mock(mocker, user_id, username):
    mock_api_client = mocker.Mock(spec=ApiClient)

    mock_api_client.get_user_data.return_value = {"user_id": user_id, "username": username}

    service = UserService(mock_api_client)

    with pytest.raises(TypeError, match="User id must be an integer"):
        service.get_username("str")

    assert service.get_username(user_id) == username.upper()

    mock_api_client.get_user_data.assert_called_once_with(user_id)