from collections import deque

idx = [[0,1],[1,0],[-1,0],[0,-1]]
def bfs(x, y, place):

    q = deque()
    q.append((x,y,0))
    visited = [[999]*5 for _ in range(5)]
    visited[x][y] = 0

    while q:

        x2, y2, dist = q.popleft()

        for each in idx:
            new_x = x2 + each[0]
            new_y = y2 + each[1]

            if 0 <= new_x < 5 and 0 <= new_y < 5 and place[new_x][new_y] != 'X':
                if visited[new_x][new_y] == 999:
                    q.append((new_x,new_y,dist + 1))
                    visited[new_x][new_y] = dist + 1

    return visited

def solution(places):

    total_result = []

    for each in places:

        P_list = []
        for i in range(5):
            for j in range(5):

                if each[i][j] == 'P':
                    P_list.append((i,j))

        flag = False
        for x,y in P_list:
            result = bfs(x,y,each)

            for x2, y2 in P_list:

                if x == x2 and y == y2: continue

                if result[x2][y2] <= 2:
                    flag = True
                    break

            if flag:
                break

        if flag:
            total_result.append(0)
        else:
            total_result.append(1)

    return total_result