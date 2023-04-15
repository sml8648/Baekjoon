import math

def check(string, prev):
    
    if string:
        mid_pos = len(string) // 2
        mid = int(string[mid_pos])
    else:
        return True
    
    if mid and not int(prev):
        return False
    else:
        return check(string[:mid_pos], mid) and check(string[mid_pos+1:],mid)

def solution(numbers):
    
    result = []
    for each in numbers:
        
        current = bin(each)[2:]
        
        tmp = int(math.log(len(current),2)) + 1
        tmp = 2**tmp-1 - len(current)
        new_current = '0'*tmp + current
        
        mid = new_current[len(new_current) // 2]
        
        if mid and check(new_current, True):
            result.append(1)
        else:
            result.append(0)
            
    return result