import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())

matrix = []
for _ in range(n):
    tmp_list = list(map(int,input().split()))
    #tmp_list = list(map(lambda x: int(x) if x != '0' else int(1e9),input().split()))
    matrix.append(tmp_list)

result = []
for i in range(n):
    tmp_list = set(j for j in range(n))
    tmp_list = tmp_list - set([i])

    permute = list(permutations(tmp_list,n-1))

    for each in permute:

        tt = list(each)
        tt.insert(0,i)
        tt.append(i)

        tmp_sum = 0
        flag = 0
        for a,b in zip(tt,tt[1:]):
            tmp_sum += matrix[a][b]
            if matrix[a][b] == 0:
                flag = 1

        if not flag:
            result.append(tmp_sum)

print(min(result))