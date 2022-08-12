def solution(s):
    answer_list = []
    a_list = list(map(int,s.split()))
    answer_list.append(str(min(a_list)))
    answer_list.append(str(max(a_list)))
    return ' '.join(answer_list)