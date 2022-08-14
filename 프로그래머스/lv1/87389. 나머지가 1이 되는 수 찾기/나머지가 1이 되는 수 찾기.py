def solution(n):
    answer = float('inf')
    for i in range(n,0,-1):
        if n % i == 1:
            answer = i
    return answer