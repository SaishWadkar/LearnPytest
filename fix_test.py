import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# def setup_module(module):
#     print("--------------Before Test ------------")
#
# def teardown_module(module):
#     print("--------------After Test ------------")

@pytest.fixture(scope='class')
def setitup(request):
    print("------------Before Test --------")
    driver = webdriver.Chrome(ChromeDriverManager.install())
    driver.get("https://google.com")


    yield
    print("------------After Test --------")
    driver.close()

@pytest.mark.usefixtures("setitup")
class Base:
    pass

class Test_me(Base):
    def test_one(self):
        print("Test One")
