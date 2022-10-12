"""
The function below returns a human readable date and time format after receiving a cron expression 

"""
from datetime import datetime

def cron_expressor(cron):

    """
        expression validity check
    """
    # checks for whitespace in cron expression
    if len(cron.split()) != 5: return "Invalid cron expression"   
