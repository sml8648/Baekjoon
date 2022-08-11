from itertools import combinations
def solution(nums):
    answer = 0

    a_list = [1] * (50001)

    for i in range(2, int((50001) ** 0.5) + 1):
        if a_list[i]:
            for j in range(2 * i, (50001), i):
                a_list[j] = 0
    
    tmp = combinations(nums,3)
    for each in tmp:
        
        if a_list[sum(each)]:
            answer += 1
        
    return answer