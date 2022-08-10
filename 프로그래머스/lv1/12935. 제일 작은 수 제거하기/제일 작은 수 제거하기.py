def solution(arr):
    answer = []
    
    Min = min(arr)
    arr.remove(Min)
    
    if len(arr):
        answer = arr
    else:
        answer = [-1]
    return answer