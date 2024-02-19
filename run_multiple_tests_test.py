import pytest
'''
    run multiple tests by :
    1. using substring : py.test -k <substring> -v 
    2. using mark      : py.test -m <mark>
'''

def fun(x):
    return x+5

@pytest.mark.one
def test_fun():
    assert fun(4)==9

