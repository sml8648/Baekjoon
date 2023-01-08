import sys
input = sys.stdin.readline

N = int(input())
a_list = list(map(int,input().split()))
b_list = list(set(a_list))
b_list.sort()
a_dict = {}

for k in b_list:
    a_dict[k] = 0

n = 0
for k in b_list:
    a_dict[k] = n
    n += 1

for each in a_list:
    print(a_dict[each], end=' ')