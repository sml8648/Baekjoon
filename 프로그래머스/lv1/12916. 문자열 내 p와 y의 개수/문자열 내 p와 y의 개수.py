def solution(s):
    
    count = 0
    for each in s.lower():
        
        if each == 'p':
            count += 1
        elif each == 'y':
            count -= 1
        
    if not count:
        return True
    else:
        return False
