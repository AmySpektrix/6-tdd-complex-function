from lib.age_checker import *
import pytest

"""
Given a valid DOB over the age of 16 
Return "Access Granted"
"""
def test_access_granted_over_16():
    assert age_checker("2000-06-15") == "Access Granted!"

"""
Given a valid DOB under the age 16 
Return "Access Denied: You are 3 and the required age is 16 or over!"
"""
def test_access_denied_under_16():
    assert age_checker("2020-06-15") == "Access Denied: You are 3 and the required age is 16 or over!"


"""
Given an invalid type 
Return "String not entered"
"""

def test_exception_invalid_type():
    with pytest.raises(Exception) as e:
        age_checker(15)
    assert str(e.value) == "String not entered: Please enter a valid iterable"


"""
Given an invalid date format 
Return "Invalid date format entered"
"""

def test_date_formatting_exception():
    with pytest.raises(Exception) as e:
        age_checker("2020.06.15")
    assert str(e.value) == "String contians invalid formatting: Please enter a string in the format YYYY-MM-DD"
