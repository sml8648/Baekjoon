from itertools import combinations
from collections import defaultdict

def solution(orders, course):

    answer = []
    for each in course:

        menu_dict = defaultdict(int)
        for menu in orders:

            comb_list = [i for i in range(len(menu))]
            p = list(combinations(comb_list, each))
            for k in p:
                tmp_list = []

                for tt in k:
                    tmp_list.append(menu[tt])

                tmp_list.sort()

                tmp = ''.join(tmp_list)
                menu_dict[tmp] += 1

        menu_dict = dict(sorted(menu_dict.items(), key=lambda item: item[1], reverse=True))

        most_common_value = -1
        count = 0
        for key, value in menu_dict.items():

            if value == 1: continue

            if count == 0:
                answer.append(key)
                most_common_value = value
            else:
                if most_common_value == value:
                    answer.append(key)
                else:
                    break

            count += 1

    return sorted(answer)