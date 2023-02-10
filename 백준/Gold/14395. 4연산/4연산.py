import sys
from collections import deque
input = sys.stdin.readline

s, t = map(int,input().split())


if s == t:
    print(0)
    sys.exit()

que = deque()
que.append(('',s))
visited = set()
visited.add(s)

flag = False
result = []
while que:

    operator, now = que.popleft()

    if now > int(1e9): continue

    if now == t:
        flag = True
        break

    for i in range(4):

        if i == 0:
            tmp = now * now
            if tmp not in visited:
                que.append((operator+'*', tmp))
                visited.add(tmp)
        elif i == 1:
            tmp = now + now
            if tmp not in visited:
                que.append((operator + '+', tmp))
                visited.add(tmp)
        elif i == 2:
            tmp = now - now
            if tmp not in visited:
                que.append((operator + '-', tmp))
                visited.add(tmp)
        elif i == 3:
            if now == 0: continue
            tmp = 1
            if tmp not in visited:
                que.append((operator + '/', tmp))
                visited.add(tmp)

if flag:
    print(operator)
else:
    print(-1)
