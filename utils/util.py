import time

def string_toTimestamp(st):
    return time.mktime(time.strptime(st, "%Y-%m-%d"))