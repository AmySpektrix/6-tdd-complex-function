from datetime import *
from dateutil.relativedelta import *

def age_checker(dob):
    if type(dob) != str:
        raise Exception("String not entered: Please enter a valid iterable")
    try:
        date.fromisoformat(dob)
    except ValueError:
        raise ValueError("String contians invalid formatting: Please enter a string in the format YYYY-MM-DD")
    dob_datetime = datetime.strptime(dob,"%Y-%m-%d")
    today = date.today()
    age_from_dob = relativedelta(today,dob_datetime).years
    if age_from_dob < 16:
        return f"Access Denied: You are {age_from_dob} and the required age is 16 or over!"
    else:
        return "Access Granted!"
