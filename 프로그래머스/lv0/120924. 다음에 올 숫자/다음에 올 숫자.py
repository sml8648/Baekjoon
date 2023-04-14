def solution(common):
    
    first, second, third = common[0], common[1], common[2]
    
    flag = True
    if second - first == third - second:
        flag = False
    elif second // first == third // second:
        flag = True
    
    if flag:
        
        return common[-1]*(second // first)
    else:
        return common[-1] + (second - first)