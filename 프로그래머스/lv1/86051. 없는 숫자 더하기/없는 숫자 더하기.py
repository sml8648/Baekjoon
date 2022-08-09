def solution(numbers):
    answer = -1
    base_set = set([i for i in range(10)])
    answer_set = set(numbers)
    
    answer = sum(base_set - answer_set)
    return answer