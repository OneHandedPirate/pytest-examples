import pytest

from examples.example3 import DB


@pytest.fixture
def db():
    database = DB()
    yield database
    database.data.clear()


@pytest.fixture
def test_user() -> str:
    return "test_user"


@pytest.fixture
def test_id() -> int:
    return 1


def test_add_user(db, test_user, test_id):
    with pytest.raises(TypeError, match="User id must be integer"):
        db.add_user("not_an_integer", "Alice")
    with pytest.raises(TypeError, match="Name must be a string"):
        db.add_user(1, 2)

    db.add_user(test_id, test_user)

    assert db.get_user(test_id) == test_user

    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(test_id, test_user)


def test_delete_user(db, test_user, test_id):
    db.add_user(test_id, test_user)
    assert db.get_user(test_id) == test_user

    db.delete_user(test_id)
    with pytest.raises(ValueError, match="User not found"):
        db.get_user(test_id)
