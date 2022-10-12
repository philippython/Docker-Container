"""
The function below returns a human readable date and time format after receiving a cron expression 

"""
from datetime import datetime


def min_hr_mon_validator(index, cron):
    try :
        int(cron.split()[index])
    except ValueError:
        pass
    else:
        if index == 0 :
            if int(cron.split()[index]) > 59 : return "Invalid minute"
        elif index == 1 :
            if int(cron.split()[index]) > 23 : return "Invalid hour"
        elif index == 2 :
            if int(cron.split()[index]) > 31 and int(cron.split()[3]) != 4 : return "Invalid minute"





def cron_expressor(cron):

    """
        expression validity check
    """
    # checks for whitespace in cron expression
    if len(cron.split()) != 5 : return "Invalid cron expression"  

    #  checks for invalid minute
    try :
        int(cron.split()[0])
    except ValueError:
        pass
    else:
        if int(cron.split()[0]) > 59 : return "Invalid minute"

print(cron_expressor('60 * * * *'))