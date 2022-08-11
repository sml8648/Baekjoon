from itertools import combinations
def solution(numbers):
    answer = []
    
    tmp = combinations(numbers,2)
    for each in tmp:
        answer.append(sum(each))
        
    answer = list(set(answer))
    answer.sort()
    return answer