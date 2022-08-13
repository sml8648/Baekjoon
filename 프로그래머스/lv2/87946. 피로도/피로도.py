from itertools import permutations
def solution(k, dungeons):
    answer = -1
    a_list = [i for i in range(len(dungeons))]
    
    tmp = permutations(a_list)
    max_value = -1
    for each in tmp:
        tmp_k = k
        tmp_count = 0
        for i in each:
            
            if tmp_k >= dungeons[i][0]:
                tmp_k -= dungeons[i][1]
                tmp_count += 1
            else:
                break
        
        if tmp_count > max_value:
            max_value = tmp_count
            
    return max_value