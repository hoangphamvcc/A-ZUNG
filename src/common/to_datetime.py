from datetime import datetime
a = 'Fri, 05 Apr 2024 09:00:34 +0700'

b = datetime.strptime(a, '%a, %d %b %Y %H:%M:%S %z').isoformat()


def datetimestr_to_datetime(datetime_str):
    return datetime.strptime(datetime_str, '%m/%d/%y/%H:%M:%S')
