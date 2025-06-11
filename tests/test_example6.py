import pytest
from examples.example6 import save_user


def test_save_user_success(mocker):
    mock_connect = mocker.patch("examples.example6.sqlite3.connect")

    mock_conn = mocker.Mock()
    mock_connect.return_value = mock_conn

    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor

    name = "Alice"
    age = 30
    save_user(name, age)

    mock_connect.assert_called_once_with("example6.db")

    mock_conn.cursor.assert_called_once()

    mock_cursor.execute.assert_any_call(
        "CREATE TABLE IF NOT EXISTS users (name text, age integer)"
    )
    mock_cursor.execute.assert_any_call("INSERT INTO users VALUES (?, ?)", (name, age))

    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()


def test_save_user_invalid_name_type():
    with pytest.raises(TypeError, match="Name must be a string"):
        save_user(123, 30)


def test_save_user_invalid_age_type():
    with pytest.raises(TypeError, match="Age must be an integer"):
        save_user("Bob", "thirty")


def test_save_user_float_age():
    with pytest.raises(TypeError, match="Age must be an integer"):
        save_user("Charlie", 25.5)
