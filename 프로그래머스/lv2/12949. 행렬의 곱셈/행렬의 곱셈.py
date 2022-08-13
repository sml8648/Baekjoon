def solution(arr1, arr2):
    
    new_arr2 = list(map(list,zip(*arr2)))

    result = []
    for each in arr1:
        tmp_arr = []
        for k in new_arr2:
            tmp_sum = 0
            for a,b in zip(each, k):
                tmp_sum += a*b
            tmp_arr.append(tmp_sum)
        result.append(tmp_arr)
        
    return result