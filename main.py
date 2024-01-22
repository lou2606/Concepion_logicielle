import datetime
from dateutil import tz


def get_time_now():
    """

    :return: str
    heure minute et seconde ('HH:MM:SS')
    """
    time = datetime.datetime.now().time()
    return str(time)[:-7]
