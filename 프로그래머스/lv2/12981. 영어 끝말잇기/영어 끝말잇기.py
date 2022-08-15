import math

def solution(n, words):
    answer = []
    
    words_set = set()
    before_word = ''
    result = -1
    for idx, each in enumerate(words):
        if idx == 0:
            words_set.add(each)
            before_word = each
            continue

        if before_word[-1] != each[0] or each in words_set:
            result = idx
            break
        else:
            words_set.add(each)
            before_word = each
            
    if result == -1:
        return [0,0]
    else:
        result = result + 1
        if result % n == 0:
            answer.append(n)
        else:
            answer.append(result % n)
        
        answer.append(math.ceil(result / n))
    return answer