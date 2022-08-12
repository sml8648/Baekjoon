def solution(s):
    answer = ''
    
    tmp = s.split(' ')
    result = []
    for each in tmp:
        
        if len(each) == 0:
            result.append('')
        else:
            result.append(each[0].upper() + each[1:].lower())

    return ' '.join(result)