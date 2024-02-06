from datetime import *
from dateutil.relativedelta import *
import re 

def age_checker(dob):
    dob_datetime = datetime.strptime(dob,"%Y-%m-%d")
    today = date.today()
    age_from_dob = relativedelta(today,dob_datetime).years
    if age_from_dob < 16:
        return f"Access Denied: You are {age_from_dob} and the required age is 16 or over!"
    else:
        return "Access Granted!"

