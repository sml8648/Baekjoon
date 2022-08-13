def solution(d, budget):
    answer = 0
    cost = sorted(d)
    
    sum = 0
    for idx, each in enumerate(cost):
        
        sum += each
        if sum <= budget:
            answer = idx + 1
        else:
            break
    return answer