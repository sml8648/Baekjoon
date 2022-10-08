import sys
input = sys.stdin.readline

a,b = map(int,input().split())
matrix = []
for _ in range(a):
    matrix.append(list(map(int,input().split())))


polynomio = [[[0,0],[0,1],[1,0],[1,1]],
[[0,0],[0,1],[0,2],[0,3]],
[[0,0],[1,0],[2,0],[3,0]],
[[0,0],[1,0],[2,0],[2,1]],
[[0,1],[1,1],[2,1],[2,0]],
[[0,0],[0,1],[1,1],[2,1]],
[[0,0],[0,1],[1,0],[2,0]],
[[0,0],[1,0],[1,1],[2,1]],
[[0,1],[1,1],[1,0],[2,0]],
[[1,0],[1,1],[0,1],[0,2]],
[[0,0],[0,1],[1,1],[1,2]],
[[0,0],[0,1],[0,2],[1,1]],
[[0,1],[1,0],[1,1],[1,2]],
[[1,0],[1,1],[0,1],[2,1]],
[[0,0],[1,0],[2,0],[1,1]],
[[0,0],[1,0],[1,1],[1,2]],
[[1,0],[1,1],[1,2],[0,2]],
[[0,0],[0,1],[0,2],[1,0]],
[[0,0],[0,1],[0,2],[1,2]]
]

result = -1
for i in range(a):
    for j in range(b):

        for each in polynomio:
            tmp_sum = 0
            flag = 0
            for k in each:
                x = k[0] + i
                y = k[1] + j
                if 0 <= x < a and 0 <= y < b:
                    tmp_sum += matrix[x][y]
                else:
                    flag = 1

            if flag:
                continue
            else:
                if tmp_sum > result:
                    result = tmp_sum

print(result)