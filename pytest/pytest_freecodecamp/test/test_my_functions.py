import pytest
import source.my_functions as my_functions

def test_add():
    assert my_functions.add(1, 2) == 3

def test_divide():  
    assert my_functions.divide(1, 2) == 0.5 

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)    

def test_add_strings():
    assert my_functions.add("a", "b") == "ab"

# create pytest.ini in root, write folder to run
# pytest test/test_my_functions.py 
