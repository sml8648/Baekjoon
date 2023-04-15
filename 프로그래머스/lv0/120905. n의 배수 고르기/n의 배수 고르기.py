def solution(n, numlist):
    answer = [num for num in numlist if not num % n]
    return answer