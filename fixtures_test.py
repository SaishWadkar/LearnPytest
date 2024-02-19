import pytest

# @pytest.mark.ok
# def test_fun():
#     assert True
'''
    Fixtures :
    
    @pytest.fixture()
    def some_method():
        ___ before test
        yield
        ___ after test
        
    def test_something(some_method):
        pass
'''



class TestClass:

    @pytest.fixture()
    def before_after(self):
        '''
        Saish created this sample fixture!
        '''
        print("I always run before")
        yield
        print("I always run after the test")

    @pytest.mark.usefixtures("before_after")
    #@pytest.mark.xfail
    #@pytest.mark.trylast
    def test_one(self):
        print("I'm test one")
        assert True

    @pytest.mark.xfail
    #@pytest.mark.tryfirst
    @pytest.mark.skip("I want to skip")
    def test_two(self,before_after):
        #pytest.skip("Intentially skipped ")
        print("I'm test two")
        assert False
