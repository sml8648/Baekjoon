import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr = [[0] * n for _ in range(n)]
friends_dict = dict()

def allocate(id, friends):
    max_adj, max_cnt, max_x, max_y = [-1, -1, -1, -1]
    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0: continue
            cnt, adj = [0, 0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if arr[nx][ny] == 0:
                    cnt += 1
                if arr[nx][ny] in friends:
                    adj += 1
            if adj > max_adj:
                max_adj, max_cnt, max_x, max_y = adj, cnt, x, y
            elif adj == max_adj:
                if cnt > max_cnt:
                    max_cnt, max_x, max_y = [cnt, x, y]
    arr[max_x][max_y] = id

for i in range(n * n):
    row = list(map(int,input().split()))
    id = row[0]
    friends = row[1:]
    friends_dict[id] = friends
    allocate(id, friends)


result = 0
for x in range(n):
    for y in range(n):
        number = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] in friends_dict[arr[x][y]]:
                number += 1
        score = 0
        if number == 1: score = 1
        if number == 2: score = 10
        if number == 3: score = 100
        if number == 4: score = 1000
        result += score
print(result)