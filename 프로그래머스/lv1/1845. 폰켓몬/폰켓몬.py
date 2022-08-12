def solution(nums):
    answer = 0
    tmp_set = set(nums)
    
    if len(tmp_set) >= (len(nums) // 2):
        answer = len(nums) // 2
    else:
        answer = len(tmp_set)
    
    return answer