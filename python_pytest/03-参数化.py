import pytest

@pytest.mark.parametrize('test_input, expected', [
    ('3+5', 8),
    ('2+4', 6),
    ('6*9', 54),
], ids=['case1', 'case2', 'case3'])
def test_eval(test_input, expected):
    assert eval(test_input) == expected