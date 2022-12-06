import sys
input =sys.stdin.readline

N,M = map(int,input().split())
matrix = [list(input().strip()) for _ in range(N)]
parent = [i for i in range(N*M)]

def find_parent(parent, x):

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(N*M):
    x = i // M
    y = i % M
    direction = matrix[x][y]

    if direction == 'D':
        nx = x + 1
        ny = y
    elif direction == 'U':
        nx = x - 1
        ny = y
    elif direction == 'L':
        nx = x
        ny = y - 1
    elif direction == 'R':
        nx = x
        ny = y + 1

    next_num = nx*M + ny

    if 0 <= next_num <= N*M:
        union_parent(parent, i, next_num)

visited = set()
for i in range(N*M):

    if find_parent(parent, parent[i]) not in visited:
        visited.add(parent[i])

print(len(visited))