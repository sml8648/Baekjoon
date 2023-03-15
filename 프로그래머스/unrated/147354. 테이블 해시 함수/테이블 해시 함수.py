def solution(data, col, row_begin, row_end):
    # 이게 제일 중요하네 ㅋㅋ..
    new_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    sum_list = []
    for i in range(row_begin-1, row_end):

        tmp_sum = 0
        for k in new_data[i]:

            tmp_sum += k % (i+1)

        sum_list.append(tmp_sum)

    result = sum_list[0]

    for each in sum_list[1:]:
        result = result^each
    return result