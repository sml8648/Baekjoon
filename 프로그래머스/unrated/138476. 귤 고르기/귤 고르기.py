from collections import defaultdict

def solution(k, tangerine):
    
    int_dict = defaultdict(int)
    
    for each in tangerine:
        int_dict[each] += 1
    
    result = dict(sorted(int_dict.items(), key=lambda item: item[1], reverse=True))
    
    aa = []
    tmp_k = k
    for key, value in result.items():
        
        if tmp_k > 0:
            tmp_k -= value
            aa.append(key)
            
    return len(aa)