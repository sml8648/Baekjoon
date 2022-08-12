def solution(sizes):
    answer = 0
    max_list = []
    min_list = []
    
    for each in sizes:
        max_list.append(max(each))
        min_list.append(min(each))
    
    answer = max(max_list) * max(min_list)
    return answer