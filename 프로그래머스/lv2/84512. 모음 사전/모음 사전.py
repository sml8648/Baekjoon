from itertools import product
def solution(word):
    answer = 0
    a_list = 'AEIOU'
    
    result = []
    
    for i in range(1,6):
        tmp = list(map(list,product(a_list,repeat=i)))
        
        for each in tmp:
            aa = ''.join(each)
            result.append(aa)
    
    result.sort()
    return result.index(word)+1