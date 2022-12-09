from collections import deque

n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
c = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    de = deque()
    de.append([0,0])
    ch=[[-1]*m for i in range(n)]
    ch[0][0] = 0

    while de:

        x, y = de.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if ch[nx][ny] == -1:
                    if a[nx][ny] >= 1:
                        a[nx][ny] += 1
                    else:
                        ch[nx][ny] = 0
                        de.append([nx,ny])

count = 0
while True:
    bfs()
    cht = 0
    is_last = True
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 2:
                a[i][j] = 0
                cht += 1
            elif a[i][j] == 1:
                a[i][j] = 1
                is_last = False

    if cht >= 1:
        c += 1

    if is_last:
        count = cht
        break


print(c)
print(count)
