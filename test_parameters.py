import pytest

@pytest.mark.parametrize("a,b",[(10,20),(10,-20)])
def test_multiple(a,b):
    assert a*b==200