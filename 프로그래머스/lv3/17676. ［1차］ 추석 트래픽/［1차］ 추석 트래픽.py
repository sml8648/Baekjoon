import datetime

def solution(lines):

    time_lines = []
    for line in lines:

        tmp = line.split()
        end = tmp[1]
        new_end = datetime.timedelta(hours=int(end[:2]), minutes=int(end[3:5]), \
                                     seconds=int(end[6:8]), milliseconds=int(end[9:]))

        seconds = tmp[2].split('.')
        second = seconds[0]

        # s만 딸랑 들어오는 case가 있음 짜증 ...
        try:
            mili_s = seconds[1][:-1]
        except:
            second = second.replace('s','')
            mili_s = 0

        second_delta = datetime.timedelta(seconds=int(second), milliseconds=int(mili_s))
        if second_delta > datetime.timedelta(seconds=3): second_delta = datetime.timedelta(seconds=3)
        second_delta -= datetime.timedelta(milliseconds=1)

        start = new_end - second_delta
        time_lines.append((start, new_end))

    time_lines.sort(key=lambda x : (x[1],x[0]))

    result = []
    for i in range(len(time_lines)):
        count = 0
        start_time = time_lines[i][1]
        end_time = start_time + datetime.timedelta(milliseconds=999)

        for j in range(len(time_lines)):

            tmp_start = time_lines[j][0]
            tmp_end = time_lines[j][1]

            if start_time <= tmp_end and tmp_start <= end_time:
                count += 1

        result.append(count)

    return max(result)