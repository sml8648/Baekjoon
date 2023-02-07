import sys
input = sys.stdin.readline
n = int(input())
tmp_list = list(map(int,input().split()))
tmp_list.sort()

median1 = tmp_list[len(tmp_list) // 2]
median2 = tmp_list[(len(tmp_list) // 2) - 1]

summation = 0
for each in tmp_list:
    summation += abs(each - median1)

summation2 = 0
for each in tmp_list:
    summation2 += abs(each - median2)

if summation2 <= summation:
    print(median2)
else:
    print(median1)