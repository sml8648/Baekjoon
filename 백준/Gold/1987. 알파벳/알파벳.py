import sys
input = sys.stdin.readline

index = [[0,1],[1,0],[-1,0],[0,-1]]
count = 1

def bfs():
    global count
    queue = set([(0, 0, matrix[0][0])])

    while queue:
        x, y, z = queue.pop()
        count = max(count, len(z))

        for i in range(4):
            nx = x + index[i][0]
            ny = y + index[i][1]

            if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] not in z:
                queue.add((nx, ny, matrix[nx][ny] + z))


r, c = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(r)]

bfs()
print(count)