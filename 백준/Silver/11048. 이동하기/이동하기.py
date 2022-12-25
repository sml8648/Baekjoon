n,m = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
    for j in range(m):

        tmp_list = []
        for x, y in [(-1,0),(0,-1),(-1,-1)]:

            new_x = i + x
            new_y = j + y

            if 0 <= new_x < n and 0 <= new_y < m:
                tmp_list.append(matrix[new_x][new_y])

        if len(tmp_list) == 0:
            matrix[i][j] = matrix[i][j]
        else:
            matrix[i][j] = matrix[i][j] + max(tmp_list)

print(matrix[n-1][m-1])