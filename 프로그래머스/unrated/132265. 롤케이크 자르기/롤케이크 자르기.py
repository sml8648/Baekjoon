from collections import Counter

def solution(topping):
    
    answer = 0
    result = Counter(topping)
    tmp_set = set()
    
    for i in range(len(topping)):
        
        tmp = topping[i]
        tmp_set.add(topping[i])
        
        result[tmp] -= 1
        if result[tmp] == 0:
            del result[tmp]
            
        if len(tmp_set) == len(result.keys()):
            answer += 1
        
    return answer