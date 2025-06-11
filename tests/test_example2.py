import pytest

from examples.example2 import UserManager


@pytest.fixture(scope="module")
def user_manager():
    return UserManager()


@pytest.fixture(scope="module")
def test_user() -> str:
    return "Dmitry"


@pytest.fixture(scope="module")
def test_email() -> str:
    return "plagueismkii@gmail.com"


def test_user_manager_empty(user_manager):
    assert user_manager.get_users() == {}


def test_add_user(user_manager, test_user, test_email):
    with pytest.raises(TypeError, match="Username and email must be strings"):
        user_manager.add_user()
        user_manager.add_user("test")
        user_manager.add_user(None, "test2")
        user_manager.add_user("test")
        user_manager.add_user("test2", 1)
        user_manager.add_user(122, "test2")

    user_manager.add_user(test_user, test_email)

    with pytest.raises(ValueError, match=f"User {test_user} already registered"):
        user_manager.add_user(test_user, "plagueismkii@sdfsd.com")


def test_get_user(user_manager, test_user, test_email):
    with pytest.raises(TypeError, match="Username must be a string"):
        user_manager.get_user(1)
        user_manager.get_user({"hello": "world"})
        user_manager.get_user(True)

    with pytest.raises(ValueError, match="User not found"):
        user_manager.get_user("Not_registered_user")

    assert user_manager.get_user(test_user) == {
        "username": test_user,
        "email": test_email,
    }


def test_get_users(user_manager, test_user, test_email):
    assert user_manager.get_users() == {test_user: test_email}
