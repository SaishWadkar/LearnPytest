import pytest
'''
We can create our custom markers ,
also , we can register them to avoid warnings
Register marker in "pytest.ini" file
'''
@pytest.mark.smoke
def test_login():
    print("Login Successful")
    assert True

@pytest.mark.regression
def test_add_product():
    print("Product added Successful")
    assert True

@pytest.mark.smoke
def test_logout():
    print("Logout Successfully")
    assert True


