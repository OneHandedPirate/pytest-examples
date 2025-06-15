import pytest

from examples.example8 import add


@pytest.mark.parametrize(
    "args, sum_",
    [((1, 2, 3), 6), ((4, 5), 9), ((-4, 4, 1, -1), 0), ((111111, 111111), 222222)],
)
def test_add(args, sum_):
    assert add(*args) == sum_


@pytest.mark.parametrize("args", [("1", 1), (1, "2"), ("x", "y")])
def test_add_invalid_arguments(args):
    with pytest.raises(TypeError, match="Each argument must be an integer"):
        add(*args)


def test_add_no_arguments_passed():
    with pytest.raises(ValueError, match="You should pass at least one number"):
        add(*())
