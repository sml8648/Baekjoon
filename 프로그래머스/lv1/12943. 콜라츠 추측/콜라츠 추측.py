def solution(num):
    
    tmp = num
    count = 0
    while tmp != 1:
        
        if count == 500:
            count = -1
            break
        
        if tmp % 2 == 0:
            count += 1
            tmp = tmp // 2
        else:
            count += 1
            tmp = tmp*3 + 1
            
    return count