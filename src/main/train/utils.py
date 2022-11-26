import re
import numpy as np


def get_title(name):
    """
    This method extract title inside the name 
    """
    if re.search("Mrs", name):
        return "Mrs"
    elif re.search("Mr", name):
        return "Mr"
    elif re.search("Miss", name):
        return "Miss"
    elif re.search("Master", name):
        return "Master"
    else:
        return "Other"

def get_first_cabin(row):
    """
    This method extract fisrt character in ID 
    """
    try:
        return row.split()[0]
    except AttributeError:
        return np.nan