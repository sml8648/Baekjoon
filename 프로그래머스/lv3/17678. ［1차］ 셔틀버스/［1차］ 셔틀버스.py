import datetime
import heapq

def solution(n,t,m,timetable):

    new_timetable = []
    for each in timetable:

        tmp = datetime.timedelta(hours=int(each[:2]), minutes=int(each[3:]))
        heapq.heappush(new_timetable, tmp)

    current_time = datetime.timedelta(hours=9,minutes=0)
    interval = datetime.timedelta(minutes=t)

    candidate_list = []
    for _ in range(n):

        tmp_list = []
        for _ in range(m):

            if not len(new_timetable): break

            crew_time = heapq.heappop(new_timetable)
            if crew_time > current_time:
                heapq.heappush(new_timetable, crew_time)
            elif crew_time <= current_time:
                tmp_list.append(crew_time)

        if len(tmp_list) < m:
            candidate_list.append(current_time)
        elif len(tmp_list) == m:
            candidate_list.append(tmp_list[-1] - datetime.timedelta(minutes=1))

        current_time += interval

    answer = str(max(candidate_list)).split(':')
    if len(answer[0]) == 1:
        minutes = '0'+answer[0]
    else:
        minutes = answer[0]

    seconds = answer[1]
    return minutes + ':' + seconds