def solution(elements):
    
    new_elements = elements + elements
    summation_set = set()
    for i in range(1, len(elements)+1):
        
        for j in range(0, len(new_elements)):
            
            tmp = sum(new_elements[j:j+i])
            summation_set.add(tmp)

    return len(summation_set)