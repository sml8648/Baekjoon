import sys

input = sys.stdin.readline

a_list = []

for _ in range(7):

    a = int(input())

    if a % 2:
        a_list.append(a)

if len(a_list) == 0:
    print(-1)
else:
    print(sum(a_list))
    print(min(a_list))