import sys
from collections import defaultdict
r, c, K = map(int, input().split())

matrix = []
for _ in range(3):
    matrix.append(list(map(int,input().split())))

def matrix_transpose(matrix, row, col):

    result = []
    for i in range(col):
        tmp_result = []
        for j in range(row):
            tmp_result.append(matrix[j][i])
        result.append(tmp_result)

    return result

def matrix_count(matrix):

    dict_list = []
    max_length = 0
    for each in matrix:
        int_dict = defaultdict(int)
        for k in each:
            if k == 0: continue
            int_dict[k] += 1

        sorted_dict = dict(sorted(int_dict.items(), key=lambda item: (item[1], item[0])))

        tmp = []
        for key, value in sorted_dict.items():
            tmp.append(key)
            tmp.append(value)

        tmp = tmp[:100]

        if len(tmp) > max_length: max_length = len(tmp)

        dict_list.append(tmp)

    # zero added
    for idx, each in enumerate(dict_list):
        if len(each) != max_length:

            for _ in range(max_length - len(each)):
                dict_list[idx].append(0)

    return dict_list, max_length

operator = 'B'
count = 0
col, row = 3,3
col = len(matrix[0])
row = len(matrix)

if r <= row and c <= col and (matrix[r-1][c-1] == K):
    print(count)
    sys.exit()

# when count == 0
matrix, max_length = matrix_count(matrix)
count += 1
col = len(matrix[0])
row = len(matrix)

if r <= row and c <= col and (matrix[r-1][c-1] == K):
    print(count)
    sys.exit()

while True:

    try:
        if matrix[r-1][c-1] == K:
            break
    except:
        pass

    if count == 100:
        print(-1)
        sys.exit()

    col = len(matrix[0])
    row = len(matrix)

    if row >= col:
        matrix, max_length = matrix_count(matrix)
        count += 1

    elif col > row:
        matrix = matrix_transpose(matrix, row, col)
        matrix, max_length = matrix_count(matrix)
        col = len(matrix[0])
        row = len(matrix)
        matrix = matrix_transpose(matrix, row, col)
        count += 1

print(count)