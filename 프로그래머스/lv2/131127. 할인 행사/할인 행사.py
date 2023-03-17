from collections import Counter

def solution(want, number, discount):

    answer = 0

    tmp_dict ={}
    for i,j in zip(want,number):
        tmp_dict[i] = j
    want_count = Counter(tmp_dict)

    new_discount = discount[::-1]

    sum_cache = sum(number)

    while len(new_discount) >= sum_cache:

        tmp = len(new_discount) - 10
        tmp_counter = Counter(new_discount[tmp:])

        cal_result = tmp_counter - want_count
        if not cal_result: answer += 1
        new_discount.pop() 

    return answer