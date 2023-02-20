import sys
input = sys.stdin.readline
n, m = map(int,input().split())
j = int(input())

result = 0
left = 1
right = m
for _ in range(j):

    c = int(input())

    if c < left:

        move_to = abs(left-c)
        left -= move_to
        right -= move_to
        result += move_to

    if c > right:
        move_to = abs(right-c)
        left += move_to
        right += move_to
        result += move_to

print(result)