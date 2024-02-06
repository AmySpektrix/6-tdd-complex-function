# Age
## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.

Side effects:
- 
-

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def age_checker(dob)

"""
Convert string to datetime object using strptime
Check if DOB is over 16 - if old enough let in otherwise don't 
If incorrect format/not astring, produce error 

Parameters: (dob) YYYY-MM-DD
dob: string containing users dob in the format YYYY-MM-DD

Returns: 
- If under 16 access is denied, telling them their current age and the required age (16).

- If user aged 16 or older to say that access has been granted.

- Returns error exception when the date of birth isn't the right type or format.

Side effects:
-
-

"""

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE


"""
Given a valid DOB under the age 16 
Return "Access Granted"
"""
age_checker("2020-06-15") => ["Access Denied: You are 3 and the required age is 16 or over!"]


"""
Given a valid DOB over the age of 16 
Return "Access Granted"
"""
age_checker("2020-06-15") => ["Access Granted!"]

"""
Given a valid DOB and age 16 
Return "Access Granted"
"""
age_checker("2007-06-15") => ["Access Granted!"]


"""
Given an invalid type 
Return "String not entered"
"""
age_checker(1998-03-04) => ["String not entered"]

"""
Given an invalid date format 
Return "Invalid date format entered"
"""
age_checker("1998.03.04") => ["Invalid date format entered"]




extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!