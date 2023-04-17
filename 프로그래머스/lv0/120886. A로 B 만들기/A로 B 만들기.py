from collections import Counter
def solution(before, after):
    
    before_c = Counter(before)
    before_a = Counter(after)
    
    result = before_c and before_a
    
    if before_c == result:
        return 1
    else:
        return 0