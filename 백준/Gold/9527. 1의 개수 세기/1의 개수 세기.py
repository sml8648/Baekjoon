import sys
import math

sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def sum_one(x):
    if x <= 0:
        return 0

    power = int(math.log2(x))
    power_below = 2 ** power
    if power_below == x:
        return power * x // 2 + 1

    diff = x - power_below
    return sum_one(power_below) + diff + sum_one(diff)

A, B = map(int,input().split())
print(sum_one(B) - sum_one(A-1))