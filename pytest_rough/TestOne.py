import pytest

@pytest.mark.a
def test_number_div_by_5(input_number):
    assert input_number % 5 ==0,"Not Divisible by 5 "

def test_number_div_by_10(input_number):
    assert input_number % 10 ==0,"Not Divisible by 10 "

def test_number_div_by_9(input_number):
    assert input_number % 9 ==0,"Not Divisible by 9 "
