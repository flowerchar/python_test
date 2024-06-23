# pytest --alluredir=./result
import pytest

def test_success():
    assert 1 == 1

def test_failure():
    assert 1 == 2

def test_skip():
    pytest.skip('skip the test')

def test_error():
    raise Exception('error occurred')