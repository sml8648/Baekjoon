import sys
from collections import defaultdict
n = int(input())

for _ in range(n):
    char_dict = defaultdict(int)
    tmp_list = str(input().strip())

    tmp_list = tmp_list.replace(' ','')

    for each in tmp_list:
        char_dict[each] += 1

    max_list = []
    for each in char_dict.items():
        max_list.append(each[1])

    target = max(max_list)

    result = []
    for each in char_dict.items():
        if each[1] == target:
            result.append(each[0])

    if len(result) > 1:
        print('?')
    else:
        print(result[0])