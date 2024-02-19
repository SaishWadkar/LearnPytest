'''
 Trying out built in markers in pytest
'''

import pytest
import sys
import psutil

# default pass case

def test_pass():
    assert True

#1
@pytest.mark.skip("Unconditional skip for you !")
def test_skip():
    print("You are going to skip me , unconditionally  !")

#2
@pytest.mark.skipif(sys.version_info<(4,9) , reason="Test doesn't work for older python version")
def test_skip_if():
    print("You are going to skip me , unconditionally  !")

#3
@pytest.mark.xfail
def test_x_fail():
    assert False

#4
@pytest.mark.parametrize("username, password" ,
                         [("admin","admin123"),("Mumbai","Indians"),("Chennai","Superkings")]
                        )
def test_parameters(username,password):
    print(f"Username : {username} ")
    print(f"Password : {password} ")

'''
This function shows a number of logical CPUs in the system. 
The logical core is calculated as the number of physical cores multiplied by
the number of threads that can run on each core.
In the absence of logical core, it only counts a number of physical cores.
'''
print(f"CPU count : {psutil.cpu_count(logical=False)}") # max cores including logical = 8

print(f"CPU Utilization Percentage (as per seconds) : {psutil.cpu_percent(1)}%")


