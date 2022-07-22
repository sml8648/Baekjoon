import sys

input = sys.stdin.readline

h,m,s = map(int,input().split())

s_add = int(input())

tmp = s + s_add
tmp_1 = tmp // 60
s = tmp % 60

tmp = m + tmp_1
tmp_1 = tmp // 60
m = tmp % 60

tmp = h + tmp_1
h = tmp % 24

print(h,m,s)
