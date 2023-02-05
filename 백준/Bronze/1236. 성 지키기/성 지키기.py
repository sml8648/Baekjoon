import sys
input = sys.stdin.readline
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    tmp = str(input().strip())
    matrix.append(tmp)

row_count = 0
for each in matrix:
    if 'X' not in each:
        row_count += 1

col_count = 0
for i in range(m):

    tmp_str = ''
    for j in range(n):
        tmp_str += matrix[j][i]

    if 'X' not in tmp_str:
        col_count += 1

print(max(row_count, col_count))
