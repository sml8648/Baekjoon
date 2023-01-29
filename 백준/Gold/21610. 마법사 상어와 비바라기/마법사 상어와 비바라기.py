import sys
input = sys.stdin.readline

n, m = map(int, input().split())

clouds = [(n-1, 0), (n-1, 1), (n -2, 0), (n -2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

def rain(d, s):
    positions = []
    for cloud in clouds:
        x, y = cloud
        x = (x + dx[d - 1] * s) % n
        y = (y + dy[d - 1] * s) % n
        arr[x][y] += 1
        positions.append((x,y))
    return positions

for _ in range(m):
    d, s = map(int,input().split())
    positions = rain(d,s)
    for position in positions:
        x, y = position
        cnt = 0
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if arr[nx][ny] >= 1:
                cnt += 1
        arr[x][y] += cnt
    positions = set(positions)
    clouds = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in positions:
                clouds.append((i,j))
                arr[i][j] -= 2

answer = 0
for row in arr:
    answer += sum(row)
print(answer)