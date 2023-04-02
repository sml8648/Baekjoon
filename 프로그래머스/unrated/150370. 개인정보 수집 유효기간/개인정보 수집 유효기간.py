from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):

    answer = []

    tmp = today.split('.')
    today = datetime(year=int(tmp[0]), month=int(tmp[1]), day=int(tmp[2]))

    term_dict = {}
    for each in terms:
        tmp = each.split()
        term_dict[tmp[0]] = int(tmp[1])

    for idx, each in enumerate(privacies):
        sub_date, term = each.split()
        year, month, day = map(int,sub_date.split('.'))

        now_time = datetime(year=year, month=month, day=day)
        delta = relativedelta(months=term_dict[term])

        now_time = now_time + delta

        if now_time.day == 1:
            delta = relativedelta(months=1)
            now_time = now_time - delta
            now_time = now_time.replace(day=28)
        else:
            tmp = now_time.day
            now_time = now_time.replace(day=tmp-1)

        if today > now_time:
            answer.append(idx+1)

    return answer