a,b = map(int,input().split())

matrix = []

for _ in range(a):
    a_list = list(map(int,input().split()))
    matrix.append(a_list)

position = []

for i in range(a):
    for j in range(b):
        if matrix[i][j] == 1:
            position.append((i,j))

print(abs(position[0][0] - position[1][0]) + abs(position[0][1] - position[1][1]))