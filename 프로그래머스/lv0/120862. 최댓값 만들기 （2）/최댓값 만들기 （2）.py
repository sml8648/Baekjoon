from itertools import combinations
def solution(numbers):
    comb_list = combinations(numbers,2)
    result_list = []
    for each in comb_list:
        result_list.append(each[0]*each[1])
    return max(result_list)