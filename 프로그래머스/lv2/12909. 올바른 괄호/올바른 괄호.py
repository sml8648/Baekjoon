def solution(s):
    answer = True
    
    bucket = []
    
    for each in s:
        if each == '(':
            bucket.append(each)
        else:
            if not len(bucket):
                answer = False
            else:
                bucket.pop()
    
    if len(bucket):
        return False
    else:
        return answer