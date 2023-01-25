def check(row):
    visited = [False] * n
    for i in range(n - 1):

        if abs(row[i] - row[i + 1]) >= 2:
            return False

        if abs(row[i] - row[i + 1]) == 1:
            for j in range(l):

                if row[i] - 1 == row[i + 1]:
                    current = i + 1 + j
                    if current >= n: return False
                    if row[i + 1] != row[current]: return False

                elif row[i] + 1 == row[i + 1]:
                    current = i - j
                    if current < 0: return False
                    if row[i] != row[current]: return False

                if visited[current]: return False
                visited[current] = True

    return True

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

answer = 0
for row in arr:
    if check(row):
        answer += 1
for i in range(n):
    column = []
    for j in range(n):
        column.append(arr[j][i])
    if check(column):
        answer += 1
print(answer)