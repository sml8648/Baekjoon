def solution(s):
    answer = True
    
    if not (len(s) == 4 or len(s) == 6):
        answer = False
        
    for i in s:
        if not i.isdigit():
            answer = False
            
    return answer