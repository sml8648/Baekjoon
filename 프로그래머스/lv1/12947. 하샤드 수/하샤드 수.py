def solution(x):
    answer = True
    
    sum = 0
    for i in str(x):
        sum += int(i)
    
    if int(x) % sum == 0:
        return True
    else:
        return False