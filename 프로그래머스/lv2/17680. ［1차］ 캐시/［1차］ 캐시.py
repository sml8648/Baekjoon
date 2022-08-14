from collections import deque

def solution(cacheSize, cities):
    
    city_list = deque()
    
    total_time = 0
    for k in cities:
        
        each = k.lower()
        
        if each not in city_list:
            
            if cacheSize:
                if len(city_list) == cacheSize:

                    city_list.popleft()
                    city_list.append(each)

                else:
                    city_list.append(each)
                    
            total_time += 5
            
        else:
            
            city_list.remove(each)
            city_list.append(each)
            total_time += 1 
        
    return total_time