import pytest

@pytest.mark.dependency(depends=["test_2"])
# @pytest.mark.run(order=2)
# @pytest.mark.last
def test_1():
    a = 10
    b = 10
    assert a==b , "they are different"

@pytest.mark.dependency()
# @pytest.mark.run(order=1)
@pytest.mark.first
def test_2():
    name = "Saishs"
    data = "Saish works in Infor"
    assert name in data , f" '{name}' missing! in '{data}'" # desc prints only if assertion fails