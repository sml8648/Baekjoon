def solution(my_string, n):
    answer = ''
    for each in my_string:
        answer += each*n
    return answer