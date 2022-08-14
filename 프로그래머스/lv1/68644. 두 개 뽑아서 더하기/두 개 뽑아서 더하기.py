from itertools import combinations
def solution(numbers):
    return sorted(set(list(map(sum,combinations(numbers,2)))))