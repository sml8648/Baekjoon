def solution(s):
    answer = []
    
    tmp = s.split('},{')
    result = []
    for idx, each in enumerate(tmp):
        tmp_arr = []
        
        if len(tmp) == 1:
            aa = each[2:-2].split(',')
            tmp_arr.extend(aa)
            
        elif idx == 0:
            aa = each[2:].split(',')
            tmp_arr.extend(aa)
        
        elif idx == len(tmp) - 1:
            aa = each[:-2].split(',')
            tmp_arr.extend(aa)
        
        else:
            aa = each.split(',')
            tmp_arr.extend(aa)
        
        result.append(tmp_arr)
    
    result.sort(key=lambda x : len(x))
    #print(result)
    tmp_set = set()
    answer = []
    for each in result:
        
        for k in each:
            
            if k not in tmp_set:
                tmp_set.add(k)
                answer.append(int(k))
            
            
        
    return answer