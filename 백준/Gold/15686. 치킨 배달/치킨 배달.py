import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

one_position = []
two_position = []

for idx1, row in enumerate(matrix):
    for idx2, k in enumerate(row):

        if k == 1:
            one_position.append((idx1,idx2))
        if k == 2:
            two_position.append((idx1,idx2))

comb_two = list(combinations(two_position, M))

final_result = []
for each0 in comb_two:

    chicken_distance = []

    for each2 in one_position:
        tmp = []
        for each in each0:
            tmp.append(abs(each[0] - each2[0]) + abs(each[1] - each2[1]))

        chicken_distance.append(min(tmp))

    final_result.append(sum(chicken_distance))

print(min(final_result))