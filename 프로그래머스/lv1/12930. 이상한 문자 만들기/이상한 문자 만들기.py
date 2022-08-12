def solution(s):
    answer = []
    tmp = s.split(' ')
    
    for each in tmp:
        tmp_str = ''
        
        for idx,i in enumerate(each):
            if idx % 2 == 0:
                tmp_str += i.upper()
            else:
                tmp_str += i.lower()
        answer.append(tmp_str)
    
    return ' '.join(answer)