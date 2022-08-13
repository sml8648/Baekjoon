from collections import Counter
def solution(n):
    answer = 0
    tmp = str(bin(n))[2:]
    n_count = Counter(tmp)
    
    one_count = list(n_count.items())[0][1]
    
    new_n = n
    while True:
        new_n += 1
        aa = str(bin(new_n))[2:]
        
        new_count = Counter(aa)
        new_one = list(new_count.items())[0][1]
        
        if one_count == new_one:
            answer = new_n
            break
        
    return answer