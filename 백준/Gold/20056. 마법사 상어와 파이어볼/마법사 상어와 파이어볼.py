import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())

balls = []
for i in range(M):
    x, y, m, s, d = map(int,input().split())
    balls.append((x-1,y-1,m,s,d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move():

    arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(balls)):
        x, y, m, s, d = balls[i]
        x = (x + dx[d]*s)%N
        y = (y + dy[d]*s)%N
        arr[x][y].append((m, s, d))
        balls[i] = (x, y, m, s, d)
    return arr

def split():
    new_balls = []
    removed = set()
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) >= 2:
                removed.add((i,j))
                sum_m = 0
                sum_s = 0
                even = True
                odd = True
                for (m, s, d) in arr[i][j]:
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0: odd = False
                    if d % 2 == 1: even = False

                if odd or even: directions = [0, 2, 4, 6]
                else: directions = [1, 3, 5, 7]
                for d in directions:
                    if sum_m // 5 > 0:
                        ball = (i, j, sum_m // 5, sum_s // len(arr[i][j]), d)
                        new_balls.append(ball)
    return removed, new_balls

for _ in range(K):
    arr = move()
    removed, new_balls = split()
    for ball in balls:
        x, y = ball[:2]
        if (x, y) not in removed:
            new_balls.append(ball)
    balls = new_balls

answer = 0
for ball in balls:
    answer += ball[2]
print(answer)