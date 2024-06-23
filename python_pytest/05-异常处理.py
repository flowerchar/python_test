
import pytest


def test_raise():
    with pytest.raises((ZeroDivisionError, ValueError)):
        raise ValueError

def test_raise1():
    with pytest.raises(ZeroDivisionError) as excinfo:
        raise ZeroDivisionError("division by zero")
    assert excinfo.type is ZeroDivisionError
    assert excinfo.value.args[0] == "division by zero"