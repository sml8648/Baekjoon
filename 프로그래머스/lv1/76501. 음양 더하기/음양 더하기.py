def solution(absolutes, signs):
    answer = 0
    new_signs = [1 if i else -1 for i in signs]
    
    for a,b in zip(absolutes, new_signs):
        answer += a*b
        
    return answer