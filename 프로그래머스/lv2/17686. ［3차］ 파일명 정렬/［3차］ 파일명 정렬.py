import re

def solution(arr):

    parse_result = []

    head = re.compile('[a-zA-Z-. ]+')
    number = re.compile('[0-9]{1,5}')
    for idx, each in enumerate(arr):

        tmp_list = []
        tmp_list.append(idx)

        head_part = head.match(each)
        last_idx = head_part.span()[1]

        head1 = each[:last_idx]
        each = each[last_idx:]

        tmp_list.append(head1)
        tmp_list.append(head1.lower())

        number_part = number.match(each)
        last_idx = number_part.span()[1]

        number1 = each[:last_idx]
        each = each[last_idx:]

        tmp_list.append(number1)
        tmp_list.append(int(number1))
        tmp_list.append(each)

        parse_result.append(tmp_list)

    parse_result.sort(key=lambda x : (x[2],x[4],x[0]))

    final_result = []
    for each in parse_result:
        tmp_list = []
        tmp_str = ''.join([each[1],each[3],each[5]])
        final_result.append(tmp_str)
    return final_result