import datetime
import calendar
def solution(a, b):
    my_date = datetime.datetime(2016,a,b)
    result = calendar.day_name[my_date.weekday()]
    
    return result[:3].upper()