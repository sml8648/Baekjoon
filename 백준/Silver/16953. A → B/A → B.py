import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int,input().split())

que = deque()
count = 0
que.append((count,A))

result = 0
while que:

    cnt, number = que.popleft()

    if number >= B:
        result = cnt
        break

    if int(str(number) + '1') <= B:
        que.append((cnt+1,int(str(number) + '1')))

    if number * 2 <= B:
        que.append((cnt+1, number *2))


if result == 0:
    print(-1)
else:
    print(result + 1)