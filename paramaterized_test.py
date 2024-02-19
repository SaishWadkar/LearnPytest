import pytest

#@pytest.mark.xfail
@pytest.mark.parametrize("a,b,c",[(10,20,200),(20,20,200)])
def test_multiple_parameter(a,b,c):
    assert a*b == c
