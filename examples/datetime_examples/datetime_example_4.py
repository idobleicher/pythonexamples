
from datetime import date
from datetime import time
import datetime
from datetime import timedelta


def round_time(dt=None, date_delta=datetime.timedelta(minutes=1), to='closest'):
    """
    Round a datetime object to a multiple of a timedelta
    :param datetime dt: datetime object to round (default to datetime.utcnow())
    :param timedelta date_delta: interval to round to
    :param str to: rounding method - up, down, closest (default)
    """
    round_to = date_delta.total_seconds()

    if dt is None:
        dt = datetime.datetime.utcnow()

    seconds = (dt - dt.min).seconds

    if to == 'up':
        rounding = (seconds + round_to) // round_to * round_to
    elif to == 'down':
        rounding = seconds // round_to * round_to
    elif to == 'closest':
        rounding = (seconds + round_to / 2) // round_to * round_to
    else:
        raise ValueError(
            'Expected `to` to be one of: up, down, closest')

    return dt + datetime.timedelta(
        seconds=rounding - seconds,
        microseconds=-dt.microsecond)


datetime_1 = datetime.datetime.utcnow() - timedelta(days=5)
timedelta_1 =  date_delta=timedelta(days=1)

print("before round" ,datetime_1)
roundtime = round_time(datetime_1, timedelta_1   , to='down')
print("round time down" ,roundtime)
roundtime = round_time(datetime_1, timedelta_1   , to='up')
print("round time up" ,roundtime)
roundtime = round_time(datetime_1, timedelta_1   , to='closest')
print("round time closest" ,roundtime)