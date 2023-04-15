def solution(hp):
    
    answer = 0
    div, remain = divmod(hp,5)
    answer += div
    div, remain = divmod(remain,3)
    answer += div
    div, remain = divmod(remain,1)
    answer += div
    
    return answer