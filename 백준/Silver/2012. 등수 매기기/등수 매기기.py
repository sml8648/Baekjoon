import sys
input = sys.stdin.readline
n = int(input())

a_list = []

for _ in range(n):
    a = int(input())
    a_list.append(a)

result = 0
for idx, each in enumerate(sorted(a_list)):

    result += abs((idx+1) - each)

print(result)