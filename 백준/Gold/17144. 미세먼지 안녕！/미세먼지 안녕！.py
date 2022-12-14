import sys
input = sys.stdin.readline

r,c,t = map(int,input().split())

Particulates = []
Particulates_copy = [[0]*c for _ in range(r)]

for _ in range(r):
    tmp = list(map(int,input().split()))
    Particulates.append(tmp)

direction = [[0,1],[1,0],[0,-1],[-1,0]]

position = []
for i in range(r):
    for j in range(c):
        if Particulates[i][j] == -1:
            position.append((i,j))

for _ in range(t):
    for i in range(r):
        for j in range(c):

            if Particulates[i][j] > 0:

                count = 0
                for each in direction:
                    new_i = i + each[0]
                    new_j = j + each[1]

                    if 0 <= new_i < r and 0 <= new_j < c and Particulates[new_i][new_j] != -1:
                        count += 1
                        Particulates_copy[new_i][new_j] += int(Particulates[i][j] / 5)

                Particulates[i][j] -= int(Particulates[i][j] / 5) * count

    for i in range(r):
        for j in range(c):
            if Particulates_copy[i][j] > 0:
                Particulates[i][j] += Particulates_copy[i][j]
                Particulates_copy[i][j] = 0

    up = position[0]
    # Upper rotate
    for i in range(up[1]-1,-1,-1):
        if Particulates[up[0]][i+1] == -1:
            continue
        else:
            Particulates[up[0]][i+1] = Particulates[up[0]][i]

    for i in range(up[0]-1,-1,-1):
        if Particulates[i+1][0] == -1:
            continue
        else:
            Particulates[i+1][0] = Particulates[i][0]

    for i in range(1,c):
        Particulates[0][i-1] = Particulates[0][i]

    for i in range(1,up[0]+1):
        if Particulates[i][c-1] == -1:
            Particulates[i-1][c-1] = 0
        else:
            Particulates[i-1][c-1] = Particulates[i][c-1]

    for i in range(c-2, up[1]-1,-1):
        if Particulates[up[0]][i] == -1:
            Particulates[up[0]][i+1] = 0
        else:
            Particulates[up[0]][i+1] = Particulates[up[0]][i]

    dw = position[1]
    # Lower rotate
    for i in range(dw[1]-1,-1,-1):

        if Particulates[dw[0]][i+1] == -1:
            continue
        else:
            Particulates[dw[0]][i+1] = Particulates[dw[0]][i]

    for i in range(dw[0]+1,r):
        if Particulates[i-1][0] == -1:
            continue
        else:
            Particulates[i-1][0] = Particulates[i][0]

    for i in range(1,c):
        Particulates[r-1][i - 1] = Particulates[r-1][i]

    for i in range(r-2,dw[0]-1,-1):
        if Particulates[i][c-1] == -1:
            Particulates[i + 1][c - 1] = 0
        else:
            Particulates[i+1][c-1] = Particulates[i][c-1]

    for i in range(c-2, dw[1]-1,-1):
        if Particulates[dw[0]][i] == -1:
            Particulates[dw[0]][i+1] = 0
        else:
            Particulates[dw[0]][i+1] = Particulates[dw[0]][i]

total = 0
for each in Particulates:
    total += sum(each)

print(total + 2)
