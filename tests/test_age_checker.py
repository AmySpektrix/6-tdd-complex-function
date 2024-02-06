from lib.age_checker import *

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
