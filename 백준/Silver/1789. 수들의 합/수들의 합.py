import sys
input = sys.stdin.readline

s = int(input())

total = 0
count = 0
for i in range(1,s):
    count += 1
    total += i

    if s - total <= i:
        break

if s == 1:
    print(1)
else:
    print(count)