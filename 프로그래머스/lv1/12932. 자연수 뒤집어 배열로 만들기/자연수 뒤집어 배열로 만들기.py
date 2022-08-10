def solution(n):
    answer = []
    tmp = str(n)
    
    for i in tmp[::-1]:
        answer.append(int(i))
        
    return answer