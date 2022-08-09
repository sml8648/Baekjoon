rank_convert = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
def solution(lottos, win_nums):
    answer = []

    lottos_set = set(lottos)
    win_nums_set = set(win_nums)

    zero_count = -1
    if 0 in lottos_set:
        zero_count = 6 - len(lottos_set) + 1
    else:
        zero_count = 0

    win_number_count = 6 - len(win_nums_set - lottos_set)
    answer.append(rank_convert[win_number_count + zero_count])
    answer.append(rank_convert[win_number_count])
    return answer