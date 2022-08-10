def solution(n):
    answer = 0
    tmp_list = []
    for i in str(n):
        tmp_list.append(i)
    
    tmp_list.sort(reverse=True)
    answer = ''.join(tmp_list)
    return int(answer)