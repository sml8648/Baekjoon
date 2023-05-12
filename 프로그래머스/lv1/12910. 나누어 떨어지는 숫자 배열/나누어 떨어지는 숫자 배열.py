def solution(arr, divisor):
    answer = []
    
    for each in arr:
        
        if each % divisor == 0:
            answer.append(each)
    
    return sorted(answer) if len(answer) else [-1]