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
            if int(cron.split()[index]) > 31:
                return "Invalid Day of the month"
            elif int(cron.split()[3]) == 4 and int(cron.split()[index]) > 29:
                return "Invalid Day of the month"
        elif index == 3:
            if int(cron.split()[index]) > 12 : return "Invalid Month"






def cron_expressor(cron):

    """
        expression validity check
    """
    # checks for whitespace in cron expression
    if len(cron.split()) != 5 : return "Invalid cron expression"  

    #  checks for invalid minute
    for i in range(0, len(cron.split())):
        print(min_hr_mon_validator(int(i), cron))

print(cron_expressor('24 5 31 7 *'))