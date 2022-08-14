from itertools import combinations
import math

n = int(input())

for _ in range(n):
    tmp = combinations(list(map(int,input().split()))[1:],2)
    Sum = 0
    for each in tmp:
        Sum += math.gcd(each[0],each[1])
    print(Sum)