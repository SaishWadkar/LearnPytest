'''
    Special module for all fixtures.
    This module can have multiple fixtures in it.
'''
import pytest

@pytest.fixture()
def input_number():
    number = 100

    return number

