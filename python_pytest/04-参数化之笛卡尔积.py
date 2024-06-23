import pytest

@pytest.mark.parametrize('wd', ['a', 'b', 'c'])
@pytest.mark.parametrize('num', [1, 2, 3])
def test_wd(wd, num):
    print(f"wd={wd}, num={num}")