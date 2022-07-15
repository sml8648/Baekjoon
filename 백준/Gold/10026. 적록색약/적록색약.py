import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n = int(input())

matrix = []
matrix2 = []
visited = [ [False]*n for _ in range(n)]

for _ in range(n):
    tmp_list = str(input().strip())
    matrix.append(tmp_list)

    tmp_str = ''
    for each in tmp_list:

        if each == 'R' or each == 'G':
            tmp_str += 'R'
        else:
            tmp_str += each
    matrix2.append(tmp_str)

def dfs(i,j):
    
    visited[i][j] = True
    color = matrix[i][j]
    
    for x,y in [(1,0),(-1,-0),(0,-1),(-0,1)]:
        if 0 <= i+x < n and 0 <= j+y < n:
            if not visited[i+x][j+y] and matrix[i+x][j+y] == color:
                dfs(i+x,j+y)

# 귀찮아서 걍 복붙함
def dfs2(i, j):
    visited[i][j] = True
    color = matrix2[i][j]

    for x, y in [(1, 0), (-1, -0), (0, -1), (-0, 1)]:
        if 0 <= i + x < n and 0 <= j + y < n:
            if not visited[i + x][j + y] and matrix2[i + x][j + y] == color:
                dfs2(i + x, j + y)


count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count += 1
            dfs(i,j)

print(count, end=' ')
visited = [ [False]*n for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count += 1
            dfs2(i, j)

print(count)
