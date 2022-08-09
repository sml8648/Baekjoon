def solution(arr):
    answer = [-1]
    
    for each in arr:
        
        if answer[-1] != each:
            answer.append(each)

    return answer[1:]