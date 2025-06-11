import pytest

from examples.example4 import is_prime


@pytest.mark.parametrize(
    "num, expected",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (19, True),
        (25, False),
    ],
)
def test_is_prime(num, expected):
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_prime("str")
        is_prime({})
        is_prime(True)
        is_prime(0.5)
    assert is_prime(num) == expected
