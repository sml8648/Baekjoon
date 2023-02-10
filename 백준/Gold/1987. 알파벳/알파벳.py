import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

def dfs(x, y, cost):
    global result
    result = max(result, cost)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if not visited[ord(graph[nx][ny]) - 65]:
            visited[ord(graph[nx][ny]) - 65] = True
            dfs(nx, ny, cost + 1)
            visited[ord(graph[nx][ny]) - 65] = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(input())

result = 0
visited = [False] * 26
visited[ord(graph[0][0]) - 65] = True
dfs(0, 0, 1)
print(result)