from collections import defaultdict
import datetime

d1 = datetime.timedelta(hours = 6, minutes = 00)
d2 = datetime.timedelta(hours = 23, minutes = 34)

def solution(fees, records):
    
    records_dict = defaultdict(str)
    time_sum_dict = defaultdict(int)
    
    for each in records:

        time, number, direct = each.split()

        if direct == 'IN':
            records_dict[number] = time

        elif direct == 'OUT':

            in_time = records_dict[number].split(':')
            in_time = datetime.timedelta(hours=int(in_time[0]), minutes=int(in_time[1]))

            out_time = time.split(':')
            out_time = datetime.timedelta(hours=int(out_time[0]), minutes=int(out_time[1]))

            time_sum_dict[number] += ((out_time - in_time).seconds) // 60
            del records_dict[number]
    
    for key, value in records_dict.items():

        in_time = value.split(':')
        in_time = datetime.timedelta(hours=int(in_time[0]), minutes=int(in_time[1]))

        out_time = datetime.timedelta(hours=int(23), minutes=int(59))
        time_sum_dict[key] += ((out_time - in_time).seconds) // 60

    for key, value in time_sum_dict.items():

        cost = 0
        if value > fees[0]:
            
            tmp = value - fees[0]
            divider, remain = divmod(tmp, fees[2])

            if not remain:
                cost = fees[1] + fees[3]*(divider)
            else:
                cost = fees[1] + fees[3]*(divider + 1)

            time_sum_dict[key] = cost

        elif value <= fees[0]:
            time_sum_dict[key] = fees[1]

    result = dict(sorted(time_sum_dict.items(), key=lambda t: t[0]))

    answer = [each for each in result.values()]

    return answer